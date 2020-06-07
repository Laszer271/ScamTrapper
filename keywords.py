import pandas as pd
import re

df = pd.read_excel('keywords.xlsx')
df['Fraza'] = df['Fraza'].str.replace('^\s+', '').str.replace('\s+$', '')
df['Fraza'] = df['Fraza'].str.replace('\s+', ' ')
df.to_csv('keywords.csv', index=False)
'''
ids = []
keywords = []
for i, phrase in enumerate(phrases):
    alt = re.search('\([\w\W]+\)', phrase)
    if alt:
        alt = alt.group()
        keywords.append(alt)
        ids.append(df.loc[i, 'Id/słowo klucz'])
    alts = re.finditer('\/', phrase)
    alts = [alt for alt in alts]
    for alt in alts:
'''
        
