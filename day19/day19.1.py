import os
import json
import csv
import xlrd
#file handling
# many different types of files obviously (txt, csv, json)
# use open() built in function to create read update and delete
# open(filename, mode) mode is read (default), append, write, create, text, and binary mode (images, etc)
# similar to scanner class you have read(char) readline(none) readlines(number of lines) --> readlines just gives all the lines in the document, each line is a str in a list
# need to close after, like scanner, close()
f = open('./reading_file_example.txt')
lines = f.readlines() # can also do by f.read().splitlines()
print(lines)
f.close()

# can use the with method to reduce the chance that you forget to close the file, it automatically does it
with open('./reading_file_example.txt') as f:
    lines_now = f.readlines()
    print(lines_now)

# now need to use "a" or "w" for adding text
with open('./reading_file_example.txt', 'a') as j:
    j.write("I would like to be better at python!") # appends a line

with open('./creating_file_example.txt', 'w') as f:
    f.write('Dont quite know the difference between the two') # overwrites anything in the file, creates a new file if it doesnt exist

# deleting a file requires os. use a try catch block though to not have issues if the file doesn't exist
try:
    os.remove('./creating_file_example.txt')
except:
    print('The filename may be incorrect')

# JSON are JavaScript objects but also Python dictionaries
# use json module to convert it then use the loads() to convert it
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''

person_dict = json.loads(person_json)
print(person_dict)

# then, lets now do the reverse with the dumps() function

person_json_2 = json.dumps(person_dict, indent=4)
print(type(person_json_2))
print(person_json_2)

# write to a file
with open('./creating_file_example.txt', 'w', encoding='utf-8') as f:
    json.dump(person_dict, f, indent=4)

# csv is comma seperated values, very common
# use reader() method to do it

with open('./csv_example.csv') as f:
    csv_read = csv.reader(f, dialect=',')
# basically you iterate over the csv as if it were a 2d array
# csv_read is an iterator so you use it in a for loop

# using excel data 'xlsx' with the module xlrd
# open_workbook, nsheets, sheet_names

# can also read xml files pretty easily