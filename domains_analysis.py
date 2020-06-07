import pandas as pd
import server
import json
import server

if __name__ == '__main__':
    with open('sheet_ids.json') as json_file:
        SHEET_IDS = json.load(json_file)
    df = server.get_database(SHEET_IDS['all_sites'])
    df = df.loc[df['State'] == 'scam']
    domains = pd.DataFrame()
    l = list(df["Url"].str.split(pat = "."))
    lista = []
        
    for sublist in l:
        for i in range(len(sublist)-1):
            listToStr = '.'.join([str(sublist[j]) for j in range(i,len(sublist))])
            lista.append(listToStr)
            
    domains["Domain"] = lista
    domains = domains.drop_duplicates()
    domains["Count"] = 0
    def count(url, df):
        url_elements = url.split('.')
        for i in range(len(url_elements)-1):
            listToStr = '.'.join([str(url_elements[j]) for j in range(i,len(url_elements))])
            mask = df['Domain'] == listToStr
            df.loc[mask, 'Count'] += 1
      
    for val in df['Url'].values:
        count(val, domains)
    domains.sort_values(by='Count', axis=0, inplace=True, ascending=False)
    server.update_database(domains, SHEET_IDS['all_domains'], mode='upload')