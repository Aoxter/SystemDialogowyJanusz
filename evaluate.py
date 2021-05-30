from UserActType import UserActType
import os
import pandas as pd
import numpy as np
from NaturalLanguageUnderstanding import NLU

nlu = NLU()

rows = 0
hits = 0
hard_hits = 0

for file_name in os.listdir('data'):
    df = pd.read_csv(f'data/{file_name}', sep='\t', names=['interlocutor', 'sentence', 'acts'])
    df = df[df.interlocutor == 'user']
    data = np.array(df)

    for row in data:
        rows += 1
        sentence = row[1]
        acts = row[2].split('&')
        user_act = nlu.parse_user_input(sentence)
        for act in acts:
            if str(user_act) == act.strip(' '):
                hard_hits += 1
        for act in acts:
            if act.split('(')[0].strip(' ') == str(user_act).split('(')[0].strip(' '):
                hits += 1

print(f"Accuracy (intent only): {(hits / rows)*100} ({hits}/{rows})")
print(f"Accuracy (intent with slots): {(hard_hits / rows)*100} ({hard_hits}/{rows})")
