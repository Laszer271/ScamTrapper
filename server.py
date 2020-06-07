import requests
import pandas as pd
import re
from oauth2client import file, client, tools
import gspread
import gspread_dataframe as gd
import json
import os

def get_content(urls):
    contents = []
    for url in urls:
        content = requests.get(url).text
        contents.append(content)
    return contents

def save_content_to_html(df, filepath):
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    if filepath[-1] != '/':
        filepath += '/'
        
    for index, row in df.iterrows():
        with open(filepath + str(index) + '.html', 'w', encoding='utf-8') as file:
            file.write(row['Content'])

def get_database(sheet_id, storage_path='storage.json',
                    credentials_path='credentials.json',
                    sheet_name='Arkusz1', usecols=None):
    SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
    store = file.Storage(storage_path)
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(credentials_path, SCOPES)
        creds = tools.run_flow(flow, store)
    gc = gspread.authorize(creds)
    
    ws = gc.open_by_key(sheet_id).worksheet(sheet_name)
    existing = gd.get_as_dataframe(ws, usecols=usecols).dropna(how='all').dropna(axis=1, how='all')
    return existing

def update_database(df, sheet_id, storage_path='storage.json',
                    credentials_path='credentials.json',
                    sheet_name='Arkusz1', usecols=None,
                    mode='append'):
    SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
    store = file.Storage(storage_path)
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(credentials_path, SCOPES)
        creds = tools.run_flow(flow, store)
    gc = gspread.authorize(creds)
    
    ws = gc.open_by_key(sheet_id).worksheet(sheet_name)
    if mode == 'append':
        existing = gd.get_as_dataframe(ws, usecols=usecols).dropna(how='all').dropna(axis=1, how='all')
        updated = existing.append(df)
    else:
        updated = df
    gd.set_with_dataframe(ws, updated, resize=True)

if __name__ == '__main__':
    with open('sheet_ids.json') as json_file:
        SHEET_IDS = json.load(json_file)
        
    df = get_database(SHEET_IDS['all_sites'])
    df['Content'] = None
    mask = df['State'] == 'nie-scam'
    urls = df.loc[mask, 'Url']
    content = get_content(urls)
    df.loc[mask, 'Content'] = content
    df = df.loc[mask, ['Url', 'Content']]
    df.to_excel('database_with_content.xlsx', index=False)
    
    df = pd.read_excel('database_with_content.xlsx')
    save_content_to_html(df, 'websites_content')
    
    
    
