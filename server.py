import requests
import pandas as pd
import re
from oauth2client import file, client, tools
import gspread
import gspread_dataframe as gd

def get_content(urls):
    contents = []
    for url in urls:
        content = requests.get(url).text
        contents.append(content)
    return contents

def get_database(sheet_id, storage_path='storage.json',
                    credentials_path='credentials.json',
                    sheet_name='Arkusz1'):
    SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
    store = file.Storage(storage_path)
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(credentials_path, SCOPES)
        creds = tools.run_flow(flow, store)
    gc = gspread.authorize(creds)
    
    ws = gc.open_by_key(SHEET_ID).worksheet(sheet_name)
    existing = gd.get_as_dataframe(ws, usecols=[0, 1]).dropna()
    return existing

def update_database(df, sheet_id, storage_path='storage.json',
                    credentials_path='credentials.json',
                    sheet_name='Arkusz1'):
    SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
    store = file.Storage(storage_path)
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(credentials_path, SCOPES)
        creds = tools.run_flow(flow, store)
    gc = gspread.authorize(creds)
    
    ws = gc.open_by_key(SHEET_ID).worksheet(sheet_name)
    existing = gd.get_as_dataframe(ws, usecols=[0, 1]).dropna()
    updated = existing.append(df)
    gd.set_with_dataframe(ws, updated)

if __name__ == '__main__':
    '''
    keywords = pd.read_excel('keywords.xlsx', usecols=[1]).squeeze()
    keywords = [re.sub('\s', '+', keyword) for keyword in keywords]
    base_url = 'https://www.google.com/search?&q='
    urls = [base_url + keyword for keyword in keywords]
    contents = get_content(urls)
    databse = pd.DataFrame({'Url': urls, 'Content': contents})
    databse.to_excel('scams_db.xlsx', index=False)
    '''
    
    SHEET_ID = '1LX6erktlVPWjmqkUU1zD5VEPrawy6rF575mi7Ujv-EU'
    '''
    df = pd.read_excel('scams_db.xlsx', usecols=[0])
    df['State'] = 'nie-scam'
    update_database(df, SHEET_ID)
    '''
    
    df = get_database(SHEET_ID)
    
    
