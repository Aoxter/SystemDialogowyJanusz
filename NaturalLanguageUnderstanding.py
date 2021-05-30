from typing import get_args
from UserActType import UserActType
from UserAct import UserAct
from flair.data import Sentence, Token
from flair.datasets import SentenceDataset
from flair.models import SequenceTagger


class NLU:
    def __init__(self):
        self.frame_model = SequenceTagger.load('frame-model/final-model.pt')
        self.slot_model = SequenceTagger.load('slot-model/final-model.pt')

    def conllu2flair(self, sentences, label=None):
        fsentences = []
        for sentence in sentences:
            fsentence = Sentence()
            for token in sentence:
                ftoken = Token(token['form'])
                if label:
                    ftoken.add_tag(label, token[label])
                fsentence.add_token(ftoken)
            fsentences.append(fsentence)
        return SentenceDataset(fsentences)

    def get_act_type_from_intent(self, intent):
        if 'inform' in intent:
            return UserActType.INFORM
        elif 'meeting' in intent:
            if 'create' in intent:
                return UserActType.CREATE_MEETING
            elif 'update' in intent:
                return UserActType.UPDATE_MEETING
            elif 'cancel' in intent:
                return UserActType.CANCEL_MEETING
            elif 'list' in intent:
                return UserActType.MEETING_LIST
            elif 'free_time' in intent:
                return UserActType.FREE_TIME
        elif 'hello' in intent:
            return UserActType.HELLO
        elif 'bye' in intent:
            return UserActType.BYE
        elif 'confirm' in intent:
            return UserActType.CONFIRM
        elif 'negate' in intent:
            return UserActType.NEGATE
        elif 'thankyou' in intent:
            return UserActType.THANKYOU
        else:
            return UserActType.INVALID

    def get_slots(self, slots):
        arguments = []
        candidate = None
        for slot in slots:
            if slot[1].startswith("B-"):
                if(candidate != None):
                    arguments.append(candidate)
                candidate = [slot[1].replace("B-", ""), slot[0]]
            if slot[1].startswith("I-") and candidate != None and slot[1].endswith(candidate[0]):
                candidate[1] += " " + slot[0]
        if(candidate != None):
            arguments.append(candidate)
        temp_slots = [(x[0], x[1]) for x in arguments]
        final_slots = []
        description_slot = ''
        place_slot = ''
        for slot in temp_slots:
            if slot[0] == 'description':
                if description_slot != '':
                    description_slot += ' '
                description_slot += slot[1]
            elif slot[0] == 'place':
                if place_slot != '':
                    place_slot += ' '
                place_slot += slot[1]
            elif slot[0] == 'date':
                slot_value = slot[1].casefold()
                if len(slot_value) > 3:
                    final_slots.append(('date', slot_value.strip('.')))
            elif slot[0] == 'time':
                numeric = False
                for char in slot[1]:
                    if char.isdigit():
                        numeric = True
                if numeric:
                    final_slots.append(('time', slot[1].strip('.')))
            elif slot[0] == 'participant':
                if len(slot[1]) > 3:
                    final_slots.append(('participant', slot[1].strip('.')))
            else:
                final_slots.append(slot)
        if description_slot != '':
            final_slots.append(('description', description_slot.strip('.')))
        if place_slot != '':
            final_slots.append(('place', place_slot.strip('.')))
        return final_slots
    
    def analyse_user_input(self, text):
        sentence = text.translate(str.maketrans('', '', '!"#$%&\'()*+,/;<=>?@[\]^_`{|}~'))
        sentence = sentence.strip('.')
        csentence = [{'form': word} for word in sentence.split()]
        fsentence = self.conllu2flair([csentence])[0]
        self.frame_model.predict(fsentence)
        self.slot_model.predict(fsentence)
        possible_intents = {}
        for token in fsentence:
            for intent in token.annotation_layers["frame"]:
                if(intent.value in possible_intents):
                    possible_intents[intent.value] += intent.score
                else:
                    possible_intents[intent.value] = intent.score
        return [(token, ftoken.get_tag('slot').value) for token, ftoken in zip(sentence.split(), fsentence) if ftoken.get_tag('slot').value != 'O'], max(possible_intents)

    def get_user_act(self, analysis):
        slots = analysis[0]
        intent = analysis[1]
        act_type = self.get_act_type_from_intent(intent)
        slots = self.get_slots(slots)
        return UserAct(act_type, slots)

    def parse_user_input(self, text: str) -> UserAct:
        analysis = self.analyse_user_input(text)
        return self.get_user_act(analysis)
