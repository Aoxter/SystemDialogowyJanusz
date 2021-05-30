import os
import pandas as pd
import numpy as np
from flair.data import Sentence, Token
from flair.datasets import SentenceDataset
from flair.models import SequenceTagger

def conllu2flair(sentences, label=None):
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

def predict(frame_model, sentence):
    csentence = [{'form': word} for word in sentence.split()]
    fsentence = conllu2flair([csentence])[0]
    frame_model.predict(fsentence)
    possible_intents = {}
    for token in fsentence:
        for intent in token.annotation_layers["frame"]:
            if(intent.value in possible_intents):
                possible_intents[intent.value] += intent.score
            else:
                possible_intents[intent.value] = intent.score
    return max(possible_intents)

frame_model = SequenceTagger.load('frame-model/final-model.pt')

for file_name in os.listdir('data'):
    df = pd.read_csv(f'data/{file_name}', sep='\t', names=['interlocutor', 'sentence', 'acts'])
    df = df[df.interlocutor == 'user']
    data = np.array(df)

    for row in data:
        sentence = row[1]
        predicted_intent = predict(frame_model, sentence)
        print(sentence, predicted_intent)
