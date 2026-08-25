import numpy as np
import pandas as pd
import pathlib
import re

base_dir = pathlib.Path(__file__).resolve().parent.parent
csv_path = base_dir / "day19" / "hacker_news.csv"
try:  
    hacker_news = pd.read_csv(csv_path)
except:
    print('File does not exist at this location')

print(hacker_news.head())
print('----------')
print(hacker_news.tail())

headers = hacker_news.columns
print(headers)
print(type(headers))
print(hacker_news.shape)

def find_python():
    counter = 0
    for story in hacker_news:
        title = hacker_news['title']
        if 'python' or 'Python' in title: counter += 1
    return counter
print(find_python())