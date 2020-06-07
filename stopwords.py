from bs4 import BeautifulSoup
import re
import os
import pandas as pd
import utils
import server
import json

def get_words_from_wikipedia(file):
    file = open(file, 'r', encoding='utf-8')
    # read all lines at once
    all_of_it = file.read()
    # close the file
    file.close()
    # kill all script and style elements
    soup = BeautifulSoup(all_of_it, 'lxml').find('div', id='bodyContent')
    try:
        soup = soup.find_all('p')
        soup = [p.text for p in soup]
    except AttributeError:
        return None
    text = ' '.join(soup[:-1])
    text = re.sub('[\s()[\]"•·„”]+',' ', text)
    pat = '\s*[!?.,:;›\-+|\/\\\–]+\s+'
    url_pat = '\s*[^\s]+\.[^\s]+\s*'
    text = re.sub(url_pat, ' ', text)
    text = re.sub(pat, ' ', text)
    l = text.split()
    return l

if __name__ == '__main__':
    filepath = './wiki/pl/articles/a'
    articles = utils.get_files(filepath)
    
    counts = {}
    #sources = {}
    art_count = 1
    for article in articles:
        print(art_count)
        art_count += 1
        if 'Grafika~' in article or 'Dyskusja_wikipedysty~' in article:
            continue
        words = get_words_from_wikipedia(article)
        if words is None:
            continue
        phrases = {1: words}
        for i in range(2, 6):
            phrases[i] = utils.get_phrases(words, i)
        for key in phrases:
            if key in counts:
                utils.update_counts(phrases[key], counts[key])
                #utils.update_sources(phrases[key], sources[key], article)
            else:
                counts[key] = utils.update_counts(phrases[key], {})
                #sources[key] = utils.update_sources(phrases[key], {}, article)
    for key in counts:
        counts[key] = {k: v for k, v in sorted(counts[key].items(), key=lambda item: item[1], reverse=True)}
    phrase_num = 5
    n_save = 500
    temp = list(counts[phrase_num])[:n_save]
    for key in temp:
        print('='*75)
        print(f'{key}: {counts[phrase_num][key]}')
        #print('sources:', sources[phrase_num][key])
        
    df = pd.DataFrame()
    for key in counts:
        phrases = list(counts[key].keys())[:n_save]
        values = list(counts[key].values())[:n_save]
        df[f'Phrase{key}'] = phrases
        df[f'Count{key}'] = values
        
    with open('sheet_ids.json') as json_file:
        SHEET_IDS = json.load(json_file)
    server.update_database(df, SHEET_IDS['stop_phrases'], mode='upload')
        
            