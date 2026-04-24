# talking about ReGex which ive already done some of, used to find patterns in data
# in laymans terms it is an evolved command f
# Regular Expressions
import re

# re.match() tries to find a match at the beginning of the line, returns matched if found
string_to_search = 'I love to teach python and javaScript'
teach_match = re.match('I love to teach', string_to_search, re.I) # re.I ignores case
print(teach_match)
teach_span = teach_match.span()
start, end = teach_span
print(f"Matched text is: {string_to_search[start:end]}")

# re.search() looks for a match in the entire document, returns match including multi-line strings, only first instance
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
search_string = re.search('recommend', txt, re.I)
print(search_string)

# re.findall() returns a list with every match
find_language = re.findall('language', txt, re.I)
print(find_language)

find_python = re.findall('Python|python', txt) # use Regex expression to overcome not using re.I
print(find_python)

# re.sub() substitutes each instance with a string
txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing.
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs.
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

simple = re.sub('%', '', txt,)
print(simple)

# re.split() once it finds the match it splits the string where the match was and returns a list
print(re.split('\n', simple))

# Using RegEx expressions
# to define a RegEx variable you use r
regex_flag = r'apple'
txt_2 = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
print(re.findall(regex_flag, txt_2))

regex_flag_2 = r'[Aa]pple'
print(re.findall(regex_flag_2, txt_2))

# set of characters [] can do either specific characters [Aa] or [a-c] or [0-9] or [A-Z]
# escape sequence of \d or \D, they do something I dont understand, \d for digits \D for nondigits
# . means any char exept \n
# ^ means starts with
# $ means ends with
# * occurs zero or more times
# + occurs one or more times
# ? zero or one time
# exactly three char: {3}
# three or more {3,}
# {3,8}, 3 to 8
# | or operator again
# there are a lot more that are also fun
txt_3 = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
print(re.findall(r'\d', txt_3))
print(re.findall(r'\d+', txt_3))

# when ^ is used in brackets it is a negation so [^a-zA-z] means they cannot be included