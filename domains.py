import pandas as pd
df = pd.read_excel("links.xlsx")
domeny = pd.DataFrame()
l = list(df["url"].str.split(pat = "."))
lista = []
    
for sublist in l:
    for i in range(len(sublist)-1):
        listToStr = '.'.join([str(sublist[j]) for j in range(i,len(sublist))])
        lista.append(listToStr)
        
domeny["domena"] = lista
domeny = domeny.drop_duplicates()
domeny["count"] = 0
def count(url, df):
    url_elements = url.split('.')
    for i in range(len(url_elements)-1):
        listToStr = '.'.join([str(url_elements[j]) for j in range(i,len(url_elements))])
        mask = df['domena'] == listToStr
        df.loc[mask, 'count'] += 1
  
for val in df['url'].values:
    count(val, domeny)
domeny.to_excel("domains.xlsx")