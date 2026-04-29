import re
import os
import json
import csv

def count_num_of_lines(f):
    f.seek(0)
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
    