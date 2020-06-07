import pandas as pd
links = []
to_replace = "\n"
with open('links.txt', encoding='utf-8') as f:
    for line in f:
        link = line.replace(to_replace,"")
        links.append(link)
df = pd.DataFrame()
df['url'] = links
df['state'] = 'scam'
df.to_excel('links.xlsx', index=False)