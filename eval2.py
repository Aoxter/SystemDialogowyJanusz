from datetime import date
import jsgf
import pandas as pd
import numpy as np
import os

gramar = jsgf.parse_grammar_file('book.jsgf')
print(gramar)

rows = 0
matches = 0

for f in os.listdir('data'):
    dialog = pd.read_csv(f'data/{f}', sep='\t')
    dialog = dialog.loc[dialog['Interlocutor'] == 'user']

    # print(dialog)

    for index, row in dialog.iterrows():
        rows += 1
        match = gramar.find_matching_rules(row['Text'])
        if match:
            matches += 1
            print(match)
            acts = row['Acts'].split('&')
            print(acts)
        else:
            # print("not match")
            pass

print(rows)
print(matches)
