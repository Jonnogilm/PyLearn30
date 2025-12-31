# Multiline string is ''' or """
# Concatenating is with + like java
# Escape sequences are the same \n \t \' \"
# String formating is like java if you want to use a turple
# Negative indexing if you want to start from the right but -1 is the last index. Reverse without while loop: ::-1. Three args like this [0:6:2]
# find and rfind verses index and rindex. index raises an error if the string is not found.
# functions to see if strings are decimals, alphabet, digits and more. Could be helpful in if statements
# iidentifier returns if something could be a variable. could be helpful for dynamic naming? doesnt find reserved words

multi_sentance = '''This is a multiline sentance.
However, I do not understand why you would not simply use one line.'''

print(len(multi_sentance))

sentance = 'python'
a,b,c,d,e,f = sentance
print(a)
print(e)
print(a+c)

second_to_last = sentance[-2]
print(second_to_last)

sentance_last_two = sentance[4:]
sentance_last = sentance[-2:]
print(sentance_last)
print(sentance_last_two)
reversed = sentance[::-1]
print(reversed)

find_sentance = 'Python is higher level than Java'
index_of_on = find_sentance.find('on')
index_of_on_5 = find_sentance.find('on', 5, 15)
print(index_of_on)
print(index_of_on_5)

variable1 = 'sentance_last'
print(variable1.isidentifier())
variable2 = 'False'
print(variable2.isidentifier())