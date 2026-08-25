#pandas
# the project is for easy-to-use data structures and data analysis for Python
# pandas adds data structures to work with table-like data like Series and Dataframes
# a series is a column and a DataFrame is a multidimensional table made up of many series
# to make a series we use numpy to make a 1D array
import pandas as pd
import numpy as np

nums = [1,2,3,4,5]
s = pd.Series(nums)
print(s)

# you can also modify the index of the column
s_custom_series = pd.Series(nums, index=[1,2,3,4,5])
print(s_custom_series)

# however, if you create a series from a dictionary the index will be the keys of the dict
my_dict = {"name": "Jonno", "country": "Canada", "citizenship": "USA"}
dict_series = pd.Series(my_dict)
print(dict_series)

# Constant pd series
const_series = pd.Series(10, index = [1,2,3])
print(const_series)

# can also make them from range, linspace, or any other list creating function
# dataframes can be made from lists of lists
matrix = [[1,2,3],[4,5,6],[7,8,9]]
pd_dataframe = pd.DataFrame(matrix)
print(pd_dataframe)

# data using dict is the same as series though it always shows up as columns
database = {'Name': ['Asabeneh', 'David', 'John'], 'Country':['Finland', 'UK', 'Sweden'], 'City': ['Helsiki', 'London', 'Stockholm']}
database_frame = pd.DataFrame(database)
print(database_frame)

# Creating DataFrames from a list of Dictionaries is the same it just condenses into fewer entries
general = [
    {"Name": "Asabeneh", "Country":"Finland","City":"Helsinki"},
    {"Name": "David", "Country":"UK","City":"London"},
    {"Name": "John", "Country":"Sweden","City":"Stockholm"}]

general_dataframe = pd.DataFrame(general)
print(general)
general_dataframe['Height'] = [174, 180, 170]
general_dataframe['Weight'] = [74, 78, 80]
print(general_dataframe)

for person in general_dataframe:
    weight = general_dataframe["Weight"]
    height = general_dataframe["Height"]
    general_dataframe["BMI"] = weight/(height/100)**2
print(general_dataframe)

database_frame["BMI"] = round(database_frame["BMI"], 1)
print(database_frame)

