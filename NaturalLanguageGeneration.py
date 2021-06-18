from SystemAct import SystemAct
from SystemActType import SystemActType
from UserActType import UserActType
import random

class NLG:
    def __init__(self, dst):
        self.DST = dst

    def format_meeting(self, date, time, place, participants, description, format_type):
        if participants:
            participants = ', '.join(participants)
        if format_type == 'create':
            return f'Data: {date}\nCzas: {time}\nMiejsce: {place}\nUczestnicy: {participants}\nOpis: {description}'.replace('None', 'BRAK')
        elif format_type == 'update':
            return f'Data: {date}\nCzas: {time}\nMiejsce: {place}\nUczestnicy: {participants}\nOpis: {description}'.replace('None', 'BEZ ZMIAN')
        else:
            return f'Data: {date}\nCzas: {time}\nMiejsce: {place}\nUczestnicy: {participants}\nOpis: {description}'

    def generate_response(self, systemAct: SystemAct) -> str:
        dialogue_state, _, _ = self.DST.get_dialogue_state()
        print(f'Stacja dialogowa: {dialogue_state}')
        if dialogue_state == UserActType.CREATE_MEETING:
            if systemAct.getActType() == SystemActType.REQUEST:
                if 'date' in systemAct.getActParams():
                    return random.choice(['W jakim dniu ma się odbyć to spotkanie?', 'Jakiego dnia odbędzie się to spotkanie?'])
                elif 'time' in systemAct.getActParams():
                    return random.choice(['W jakim czasie ma się zacząć to spotkanie?', 'O której godzinie rozpoczyna się to spotkanie?'])
                elif 'place' in systemAct.getActParams():
                    return random.choice(['W jakim miejscu odbywać się będzie to spotkanie?', 'Gdzie ma się odbyć to spotkanie?'])
                elif 'description' in systemAct.getActParams():
                    return random.choice(['Czy mam dodać jakiś opis do tego spotkania?', 'Czy to spotkanie ma posiadać jakiś opis?'])
                elif 'participants' in systemAct.getActParams():
                    return random.choice(['Kto będzie brał udział w spotkaniu?', 'Kto będzie uczestnikiem tego spotkania?'])
            elif systemAct.getActType() == SystemActType.CONFIRM_DOMAIN:
                slots = systemAct.getActParams()
                meeting = self.format_meeting(slots['date'], slots['time'], slots['place'], slots['participants'], slots['description'], 'create')
                return random.choice([f'Czy mam dodać te spotkanie do kalendarza?\n{meeting}', f'Czy chcesz, abym dodał to spotkanie do kalendarza?\n{meeting}'])

        elif dialogue_state == UserActType.UPDATE_MEETING:
            if systemAct.getActType() == SystemActType.REQUEST:
                if False in systemAct.getActParams():
                    if 'date' in systemAct.getActParams():
                        return random.choice(['W jakim dniu odbywa się spotkanie, które chcesz edytować?', 'Podaj datę spotkania, które chcesz zmienić.'])
                    elif 'time' in systemAct.getActParams():
                        return random.choice(['O której godzinie zaczyna się spotkanie, które chcesz zmienić?', 'Podaj godzinę spotkania, które chcesz edytować.'])
                elif True in systemAct.getActParams():
                    if 'date' in systemAct.getActParams():
                        slot_name = 'datę'
                        slot_question = 'podaj nową datę.'
                    elif 'time' in systemAct.getActParams():
                        slot_name = 'godzinę'
                        slot_question = 'podaj nową godzinę rozpoczęcia tego spotkania.'
                    elif 'place' in systemAct.getActParams():
                        slot_name = 'miejsce'
                        slot_question = 'podaj nowe miejsce, w jakim odbywa się to spotkanie.'
                    elif 'description' in systemAct.getActParams():
                        slot_name = 'opis'
                        slot_question = 'podaj nowy opis tego spotkania.'
                    else:
                        slot_name = 'uczestników'
                        slot_question = 'podaj kim będą nowi uczestnicy tego spotkania.'
                    return f'Czy chcesz zmienić {slot_name} tego spotkania? Jeśli tak, to {slot_question}'
            if systemAct.getActType() == SystemActType.CONFIRM_DOMAIN:
                if 'meeting_to_update' in systemAct.getActParams():
                    response = random.choice([f'Czy to jest spotkanie które chcesz edytować?', f'Czy chcesz wprowadzić zmiany do następującego spotkania?'])
                    # TODO: pokazać prawdziwe spotkanie po ew. dodaniu DB
                    meeting = self.format_meeting('24.06.2021', '10:00', 'Kawiarnia Portowa', ['Andrzej Duda', 'Aleksander Kwaśniewski'], 'Spotkanie biznesowe w sprawie tarczy antyrakietowej', None)
                    return f'{response}\n{meeting}'
                else:
                    slots = systemAct.getActParams()
                    meeting = self.format_meeting(slots['date'], slots['time'], slots['place'], slots['participants'], slots['description'], 'update')
                    return random.choice([f'Czy chcesz wprowadzić następujące zmiany do tego spotkania?\n{meeting}', f'Czy potwierdzasz następujące zmiany w tym spotkaniu?\n{meeting}'])

        elif dialogue_state == UserActType.CANCEL_MEETING:
            if systemAct.getActType() == SystemActType.REQUEST:
                if 'date' in systemAct.getActParams():
                    return random.choice(['W jakim dniu odbywa się spotkanie, które chcesz anulować?', 'Podaj datę spotkania, które chcesz usunąć z kalendarza.'])
                elif 'time' in systemAct.getActParams():
                    return random.choice(['O której godzinie zaczyna się spotkanie, które chcesz usunąć z kalendarza?', 'Podaj godzinę spotkania, które chcesz anulować.'])
            # TODO dopracować po dodaniu DB
            if systemAct.getActType() == SystemActType.CONFIRM_DOMAIN:
                response = random.choice([f'Czy na pewno chcesz anulować następujące spotkanie?', f'Czy potwierdzasz usunięcie następującego spotkania?'])
                # TODO: pokazać prawdziwe spotkanie po ew. dodaniu DB
                meeting = self.format_meeting('24.06.2021', '10:00', 'Kawiarnia Portowa', ['Andrzej Duda', 'Aleksander Kwaśniewski'], 'Spotkanie biznesowe w sprawie tarczy antyrakietowej', None)
                return f'{response}\n{meeting}'

        elif dialogue_state == UserActType.MEETING_LIST:
            if systemAct.getActType() == SystemActType.REQUEST:
                if "date" in systemAct.getActParams():
                    return random.choice(['Z jakiego dnia chcesz przejrzeć spotkania?', 'Spotkania z jakiego dnia chciałbyś zobaczyć?'])
            elif systemAct.getActType() == SystemActType.MEETING_LIST:
                date = systemAct.getActParams()['date']
                response = random.choice([f'Dnia {date} masz zaplanowane następujące spotkania:', f'W dniu {date} odbywają się następujące spotkania:'])
                # TODO: pokazać prawdziwe spotkania po ew. dodaniu DB
                meetings = self.format_meeting(date, '10:00', 'Kawiarnia Portowa', ['Andrzej Duda', 'Aleksander Kwaśniewski'], 'Spotkanie biznesowe w sprawie tarczy antyrakietowej', None)
                self.DST.clear()
                return f'{response}\n{meetings}'

        elif dialogue_state == UserActType.FREE_TIME:
            if systemAct.getActType() == SystemActType.REQUEST:
                if 'date' in systemAct.getActParams():
                    return random.choice(['Z jakiego dnia chcesz zobaczyć wolne godziny?', 'Z jakiego dnia chciałbyś zobaczyć godziny, w których nie masz spotkań?'])
            elif systemAct.getActType() == SystemActType.FREE_TIME:
                date = systemAct.getActParams()['date']
                response = random.choice([f'W następujących godzinach, dnia {date} nie masz zaplanowanych spotkań:', f'W dniu {date} następujące godziny są wolne od spotkań:'])
                # TODO: pokazać prawdziwe godziny po ew. dodaniu DB
                meeting_hours = '00:00-08:00\n10:00-16:00\n18:00-24:00'
                self.DST.clear()
                return f'{response}\n{meeting_hours}'
    
        elif systemAct.getActType() == SystemActType.AFFIRM:
            if "update_meeting" in systemAct.getActParams():
                task_type_1 = 'zaktualizowane'
                task_type_2 = 'Zaktualizowanie'
            elif "cancel_meeting" in systemAct.getActParams():
                task_type_1 = 'odwołane'
                task_type_2 = 'Odwołanie'
            else:
                task_type_1 = 'dodane'
                task_type_2 = 'Dodanie'
            return random.choice([f'Spotkanie zostało pomyślnie {task_type_1}.', f'{task_type_2} spotkania przebiegło pomyślnie.'])
        
        elif systemAct.getActType() == SystemActType.REQMORE:
            if "create_meeting" in systemAct.getActParams():
                response = 'Tworzenie spotkania zostało przerwane. '
            elif "update_meeting" in systemAct.getActParams():
                response = 'Aktualizacja spotkania została przerwana. '
            elif "cancel_meeting" in systemAct.getActParams():
                response = 'Odwoływanie spotkania zostało przerwane. '
            else:
                response = ''
            return random.choice([f'{response}Czy mogę Ci w czymś jeszcze pomóc?', f'{response}Czy jest jeszcze coś co mogę dla Ciebie zrobić?'])
    
        else:
            if systemAct.getActType() == SystemActType.WELCOME_MSG:
                introduction = 'Nazywam się Janusz i jestem twoim asystentem kalendarza spotkań.'
                return random.choice([f'Cześć. {introduction}', f'Dzień dobry. {introduction}', f'Witam. {introduction}'])
            elif systemAct.getActType() == SystemActType.BYE:
                return random.choice(['Do widzenia.', 'Miłego dnia.'])
            elif systemAct.getActType() == SystemActType.NOT_UNDERSTOOD:
                try_again = 'Spróbuj swoją wypowiedź sformułować w inny sposób.'
                return random.choice([f'Nie rozumiem o czym mówisz. {try_again}', f'Nie zrozumiałem twojej ostatniej wypowiedzi. {try_again}', f'Twoja ostatnia prośba była dla mnie nie zrozumiała. {try_again}'])
        raise Exception("SystemAct:{} not recognized".format(systemAct))
