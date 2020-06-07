import pandas as pd
import json
import utils
import server

if __name__ == '__main__':
    filepath = './content'
    sites = utils.get_files(filepath)
    
    counts = {}
    site_count = 1
    for site in sites:
        print(site_count)
        site_count += 1
        words = utils.get_words(site)
        if words is None:
            continue
        phrases = {1: words}
        for i in range(2, 6):
            phrases[i] = utils.get_phrases(words, i)
        for key in phrases:
            if key in counts:
                utils.update_counts(phrases[key], counts[key])
            else:
                counts[key] = utils.update_counts(phrases[key], {})
    for key in counts:
        counts[key] = {k: v for k, v in sorted(counts[key].items(), key=lambda item: item[1], reverse=True)}
    phrase_num = 5
    n_save = 200
    temp = list(counts[phrase_num])[:n_save]
    for key in temp:
        print('='*75)
        print(f'{key}: {counts[phrase_num][key]}')
        
    df = pd.DataFrame()
    for key in counts:
        phrases = list(counts[key].keys())[:n_save]
        values = list(counts[key].values())[:n_save]
        df[f'Phrase{key}'] = phrases
        df[f'Count{key}'] = values
        
    with open('sheet_ids.json') as json_file:
        SHEET_IDS = json.load(json_file)
    server.update_database(df, SHEET_IDS['phrase_sugestions'], mode='upload')