from datetime import date
import jsgf
import pandas as pd
import numpy as np
import os
from NaturalLanguageUnderstanding import NLU

nlu = NLU()

gramar = jsgf.parse_grammar_file('book.jsgf')
print(gramar)

rows = 0
matches = 0

for f in os.listdir('data'):
    dialog = pd.read_csv(f'data/{f}', sep='\t')
    dialog = dialog.loc[dialog['Interlocutor'] == 'user']

    for index, row in dialog.iterrows():
        rows += 1
        match = gramar.find_matching_rules(row['Text'])
        if match:
            acts = row['Acts'].split('&')
            for act in acts:

                frame = nlu.parse_user_input(row['Text'])
                frame_act_name = frame.getActType().name.lower()
                if frame_act_name in act.strip():
                    matches += 1


print("Rows processed: " + str(rows))
print("Accuracy: " + str(matches/rows*100))
