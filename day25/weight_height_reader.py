import numpy as np
import pandas as pd

dataframe = pd.read_csv('weight-height.csv')
print(dataframe.head()) #only the first five rows

print(dataframe.tail()) #last five
print(dataframe.shape) # same as numpy array
print(dataframe.columns)

# now if we want a specific series
heights = dataframe['Height'] # as if you were taking a key
print(heights.head())
print(heights.describe()) #statistical information about height data, can also do for an entire dataframe
print(heights.info())