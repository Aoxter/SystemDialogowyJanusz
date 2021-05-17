import os
import re
import jsgf
import pandas as pd
import numpy as np
from NaturalLanguageUnderstanding import NLU

nlu = NLU()

rows = 0
hits = 0

for file_name in os.listdir('data'):
    df = pd.read_csv(f'data/{file_name}', sep='\t', names=['interlocutor', 'sentence', 'acts'])
    df = df[df.interlocutor == 'user']
    data = np.array(df)

    for row in data:
        sentence = row[1]
        sentences = sentence.split(',')
        for sentence in sentences:
            acts = row[2].split('&')
            for act in acts:
                rows += 1
                frame = nlu.parse_user_input(sentence)
                frame_act_name = frame.getActType().name.lower()
                if frame_act_name in act.strip():
                    hits += 1

print(f"Accuracy: {(hits / rows)*100}")
