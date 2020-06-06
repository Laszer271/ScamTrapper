from bs4 import BeautifulSoup
import re
import os
import collections
import six

def get_files(input_path, ext='html'):
    final_images_paths = []
    
    items = []
    temp_items = []
    ext_len = len(ext) + 1

    if is_iterable(input_path):
        temp_items.extend(input_path)
    else:
        temp_items.append(input_path)
    
    while len(temp_items):
        items = temp_items
        temp_items = []
        
        for item in items:
            extension = item[-ext_len:]
            if extension != f'.{ext}':
                # we assume that item is actually a directory
                new_items = os.listdir(item)
                for new_item in new_items:
                    temp_items.append(item + f'/{new_item}')
            else:
                final_images_paths.append(item)
    
    return final_images_paths

def is_iterable(arg):
    return (
        isinstance(arg, collections.Iterable) 
        and not isinstance(arg, six.string_types)
    )

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
    text = re.sub('[\s,.?!:;()[\]"]+•',' ', text)
    l = text.split()
    return l
    
def get_words(file):
    file = open(file, 'r', encoding='utf-8')
    # read all lines at once
    all_of_it = file.read()
    # close the file
    file.close()
    # kill all script and style elements
    soup = BeautifulSoup(all_of_it, 'lxml').text
    text = ' '.join(soup[:-1])
    text = re.sub('[\s,.?!:;()[\]"]+•',' ', text)
    l = text.split()
    return l

def get_phrases(words, words_num):
    grouped_words = [' '.join(words[i: i + words_num]) for i in range(0, len(words) - words_num)]
    return grouped_words

def update_counts(phrases, current_counts):
    for phrase in phrases:
        if phrase not in current_counts:
            current_counts[phrase] = 1
        else:
            current_counts[phrase] += 1
    return current_counts

def update_sources(phrases, current_sources, source):
    for phrase in phrases:
        if phrase not in current_sources:
            current_sources[phrase] = [source]
        else:
            current_sources[phrase].append(source)
    return current_sources


if __name__ == '__main__':
    #filepath = './test.html'
    filepath = './wiki/pl/articles/a'
    articles = get_files(filepath)
    
    counts = {}
    sources = {}
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
            phrases[i] = get_phrases(words, i)
        for key in phrases:
            if key in counts:
                update_counts(phrases[key], counts[key])
                update_sources(phrases[key], sources[key], article)
            else:
                counts[key] = update_counts(phrases[key], {})
                sources[key] = update_sources(phrases[key], {}, article)
    for key in counts:
        counts[key] = {k: v for k, v in sorted(counts[key].items(), key=lambda item: item[1], reverse=True)}
    phrase_num = 2
    temp = list(counts[phrase_num])[:100]
    for key in temp:
        print('='*75)
        print(f'{key}: {counts[phrase_num][key]}')
        #print('sources:', sources[phrase_num][key])
    