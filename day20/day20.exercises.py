import requests
import re

def find_most_common_words(url, num):
    request = requests.get(url)
    if request.status_code == 200:
        words = re.findall(r'[a-zA-Z]+', request.text.lower())
    else:
        print('URL is not valid')
    word_tracking = {}
    html_tags = [
    "html","head","body","title","meta","link","style","script",
    "p","br","hr","h1","h2","h3","h4","h5","h6",
    "span","div","strong","em","b","i","u","small","mark",
    "a","img","video","audio","source","iframe","canvas","svg",
    "ul","ol","li","dl","dt","dd",
    "table","tr","td","th","thead","tbody","tfoot",
    "form","input","label","textarea","select","option",
    "button","fieldset","legend",
    "header","nav","main","section","article","aside","footer"]
    for word in words:
        if word in html_tags:
            continue  # skip HTML tags
        word_tracking[word] = word_tracking.get(word, 0) + 1

    cleaned_words = list(set(word_tracking)-set(word_tracking))
    sorted_list = {key: value for key, value in sorted(word_tracking.items(), key=lambda item: item[1], reverse=True)[:num]}
    return sorted_list

#print(find_most_common_words('https://www.gutenberg.org/cache/epub/1513/pg1513-images.html', 10))

#Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
    #the min, max, mean, median, standard deviation of cats' weight in metric units.
import math
import statistics
import json
def get_weight_stats(url):
        response = requests.get(url)
        data = response.json()
        max_val = 0
        min_val = float('inf')
        lst_of_data = []
        for cat in data:
            lst = re.findall(r'\d+', cat["weight"]["metric"])
            lst_of_int = [int(num) for num in lst]
            small, large = lst_of_int
            lst_of_data.append((small+large)/2)
            max_val = max(max_val, large)
            min_val = min(min_val, small)
        
        return [min_val, max_val, statistics.mean(lst_of_data), statistics.median(lst_of_data) ,statistics.stdev(lst_of_data)]

    # the min, max, mean, median, standard deviation of cats' lifespan in years.
def get_lifespan_stats(url):
    resource = requests.get(url)
    data = resource.json()
    lst_of_data = []
    max_val = 0
    min_val = float('inf')
    for cat in data:
        lst = re.findall(r'\d+', cat["life_span"])
        lst_of_int = [int(num) for num in lst]
        small, large = lst_of_int
        lst_of_data.append((small+large)/2)
        max_val = max(max_val, large)
        min_val = min(min_val, small)
        
    return [min_val, max_val, statistics.mean(lst_of_data), statistics.median(lst_of_data) ,statistics.stdev(lst_of_data)]
  
    # Create a frequency table of country and breed of cats
from collections import Counter

def cats_from_countries(url):
    resource = requests.get(url)
    data = resource.json()
    lst_of_countries = []
    for cat in data:
        lst_of_countries.append(cat['origin'])
    return Counter(lst_of_countries)
print(get_weight_stats('https://api.thecatapi.com/v1/breeds'))
print(get_lifespan_stats('https://api.thecatapi.com/v1/breeds'))
print(cats_from_countries('https://api.thecatapi.com/v1/breeds'))

# the 10 largest countries
def get_country_large(url):
    information = requests.get(url)
    data = information.json()
    top10 = {}
    min_of_list = ('key', 0)
    for country in data:
        country_name = country["name"]["common"]
        country_population = country["population"]
        min_key, min_value = min_of_list
        if min_value < country_population and len(top10) == 10:
            top10.pop(min_key) # need to make not raise key error
            top10.setdefault(country_name, country_population)
            min = 0
            for key, value in top10.items():
                if value < min:
                    min_of_list = (key, value)
        else:
            top10.setdefault(country_name, country_population)
            if len(top10) == 10:
                for key, value in top10.items():
                    if value < min:
                        min_of_list = (key, value)
    return top10
print(get_country_large('https://restcountries.com/v3.1/all?fields=name,population'))

#the 10 most spoken languages

#the total number of languages in the countries API