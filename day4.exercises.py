string1 = 'Thirty'
string2 = 'Days'
string3 = 'Of'
string4 = 'Python'

full_string = string1 + ' ' + string2 + ' ' + string3 + ' ' + string4

str1 = 'Coding'
str2 = 'For'
str3 = 'All'

full_2_string = str1 + ' ' + str2 + ' ' + str3

company = full_2_string
print(company)
print(len(company))
company = company.upper()
print(company)
company = company.lower()
print(company)
company = company.capitalize()
print(company)
company = company.title()
print(company)
company = company.swapcase()
print(company)
company = company[6:]
print(company)

print(full_2_string.find('Coding') >= 0)
replaced_2_string = full_2_string.replace('Coding', 'Cooking', -1)
print(replaced_2_string)

python_string = 'Python for Everyone'
python_string = python_string[0:python_string.index('E')] + 'All'
print(python_string)

split_string = python_string
split_1, split_2, split_3 = split_string.split(' ', -1)
print(split_1)
print(split_2)
print(split_3)

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
companies = companies.split(',')
print(companies)

char_at_start = python_string[0]
print(char_at_start)
last_index = len(python_string)-1
print(last_index)
char_at_10 = python_string[10]
print(char_at_10)

split_str_1, split_str_2, split_str_3 = python_string.split()
split_str_1 = split_str_1[0]
split_str_2 = split_str_2[0]
split_str_3 = split_str_3[0]
split_abbr = split_str_1 + split_str_2 + split_str_3

print('Coding For All'.index('C'))
print('Coding For All'.index('F'))
print('Coding For All People'.rfind('l'))
print('You cannot end a sentence with because because because is a conjunction'.find('because'))
print('You cannot end a sentence with because because because is a conjunction'.rfind('because'))
print('You cannot end a sentence with because because because is a conjunction'.replace(' because because because ', ' '))
print('Coding For All'.startswith('Coding'))
print('Coding For All'.endswith('coding'))
print('   Coding For All      '.strip())

# thirty_days_of_python returns true

list_1 = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
cleaned_list = "# ".join(list_1)
print(cleaned_list)

string_escape = 'I am enjoying this challenge. \nI just wonder what is next.'
print(string_escape)

string_tab = 'Name\tAge\tCountry\tCity'
string_tab_2 = 'Asabeneh  250\tFinland   Helsinki'
print(string_tab)
print(string_tab_2)

radius = 10
pi = 3.14
print('radius = {}'.format(radius))
print('area = {} * radius ** {}'.format(pi, 2))
print('The area of a circle with radius {} is {} meters square'.format(radius, int(pi*radius**2)))

num1 = 8
num2 = 6
print(f'{num1} + {num2} = {num1+num2}')
print(f'{num1} - {num2} = {num1-num2}')
print(f'{num1} * {num2} = {num1*num2}')
print(f'{num1} / {num2} = {num1/num2}')
print(f'{num1} % {num2} = {num1%num2}')
print(f'{num1} // {num2} = {num1//num2}')
print(f'{num1} ** {num2} = {num1**num2}')