# Variables

languages = ['C++', 'OhCaml', 'Python', 'Java']
my_first_program = 'C++'
version = '10.1'
versions = {8.1,10,10,1}
versions_i_have_used = (10, 10.1)
version_as_number = float(version)
length_of_language = len(my_first_program)
version_rounded = int(version_as_number)

# Multiple declarations in one line
ticket, number_sold, price, discount_price, sold_out = 'Anderson Paak', 50, 75.0, 50, False

print(type(languages))
print(type(versions))
print(type(versions_i_have_used))
print(version_as_number)
print('Rounded: ', version_rounded)
print('Length: ', length_of_language)
