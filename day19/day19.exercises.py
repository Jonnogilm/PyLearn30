import re
import os
import json
import csv

def count_num_of_lines(f):
    f.seek(0) # ensures cursor isnt at EOF end of file
    lines = f.readlines()
    return len(lines)

def count_num_of_words(f):
    f.seek(0) # ensures cursor isnt at EOF end of file
    list_of_words = []
    get_line_list = f.readlines()
    for line in get_line_list:
        list_of_words.extend(list(re.findall(r'[a-zA-Z]+', line)))
    return len(list_of_words)


with open('./donald_speech.txt') as f:
    print(f'Donald lines: {count_num_of_lines(f)}')
    print(f'Donald words: {count_num_of_words(f)}')

with open('./obama_speech.txt') as f:
    print(f'Obama lines: {count_num_of_lines(f)}')
    print(f'Obama words: {count_num_of_words(f)}')

with open('./michelle_obama_speech.txt') as f:
    print(f'Michelle lines: {count_num_of_lines(f)}')
    print(f'Michelle words: {count_num_of_words(f)}')

with open('./melina_trump_speech.txt') as f:
    print(f'Melina lines: {count_num_of_lines(f)}')
    print(f'Melina words: {count_num_of_words(f)}')
    
def most_spoken_languages(filename, number_of_countries):
    with open(filename, 'r',encoding='utf-8') as f:
        dict_of_countries = json.load(f)
    tracking_dict = {}
    for country in dict_of_countries:
        for language in country['languages']:
            if language in tracking_dict:
                tracking_dict[language] += 1
            else:
                tracking_dict.setdefault(language, 1)
    sorted_tracking_dict = {key: value for key, value in sorted(tracking_dict.items(), key=lambda item: item[1], reverse=True)[:number_of_countries]}
    return sorted_tracking_dict

print(most_spoken_languages("./country_data.json", 10))
print(most_spoken_languages("./country_data.json", 3))

def most_populated_countries(filename, num_of_countries):
    with open(filename, 'r', encoding='utf-8') as f:
        country_iterable = json.load(f)
    tracking_population = []
    #for country in country_iterable:
        #dict_with_country = 

'''def extract_email_addresses(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    lst_of_addresses = []
    for line in lines:
        lst_of_addresses.extend(re.findall(r'^(?!from).*?([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})', line, re.I))
    return lst_of_addresses
print(extract_email_addresses('./email_exchanges_big.txt'))'''

def find_most_common_words(to_look, num):
    if os.path.exists(to_look):
        with open(to_look, 'r') as f:
            list_of_lines = f.readlines()
            words = [word for line in list_of_lines for word in re.findall(r'[a-zA-Z]+', line)]
    else:
        words = re.findall([r'[a-zA-Z]+', to_look])    
    word_tracking = {}
    for word in words:
        if word in word_tracking:
            word_tracking[word] += 1
        else:
            word_tracking.setdefault(word, 1)
    sorted_list = {key: value for key, value in sorted(word_tracking.items(), key=lambda item: item[1], reverse=True)[:num]}
    return sorted_list

print(find_most_common_words('./donald_speech.txt', 10))
print(find_most_common_words('./michelle_obama_speech.txt', 10))
print(find_most_common_words('./obama_speech.txt', 10))
print(find_most_common_words('./melina_trump_speech.txt', 10))

stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up',
              'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

def clean_most_common_words(dict_of_common):
    return {word: count for word, count in dict_of_common.items() if word not in stop_words}

def find_text_similarity(text1, text2):
    cleaned_top_100_1 = clean_most_common_words(find_most_common_words(text1, 100))
    cleaned_top_100_2 = clean_most_common_words(find_most_common_words(text2, 100))
    record = 0
    for key in cleaned_top_100_1:
        if key in cleaned_top_100_2:
            record +=1
    return record/(len(cleaned_top_100_1) if len(cleaned_top_100_1) > len(cleaned_top_100_2) else len(cleaned_top_100_2))

print(find_text_similarity('./melina_trump_speech.txt', './michelle_obama_speech.txt'))

#most repeated in romeo and juliet
print(find_most_common_words('./romeo_and_juliet.txt', 10))

def count_python(filename_csv):
    with open(filename_csv, 'r') as f:
        lines = [line.strip() for line in f]
        count_row = 0
        for line in lines:
            if bool(re.search(r'[Pp]ython', line)):
                count_row += 1
    return count_row
        

def count_js(filename_csv):
    with open(filename_csv, 'r', newline="", encoding="utf-8") as f:
        csv_read = csv.reader(f)
        count_row = 0
        for row in csv_read:
            if bool(re.search(r'[Pp]ython', row)):
                count_row += 1
# Java and not JavaScript
def count_java(filename_csv):
    with open(filename_csv, 'r', newline="", encoding="utf-8") as f:
        csv_read = csv.reader(f)
        count_row = 0
        for row in csv_read:
            if bool(re.search(r'[Pp]ython', row)):
                count_row += 1
print(count_python('./hacker_news.csv'))