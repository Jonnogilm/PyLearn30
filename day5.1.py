# Index lists the same way you index a string

lst = ['banana', 'orange', 'mango', 'lemon','lime','apple']
second_to_last = lst[-2]
first_item, second_item, *rest = lst #rest can be any name just needs to have the asterisk
print(rest)

ma, co, ca, nm, *west, gb = ['Massachussets', 'Colorado', 'California', 'New Mexico', 'South Dakota', 'Illinois', 'Great Britain']
print(west)

fruits = ['banana', 'orange', 'mango', 'lemon', 'beans']
all_fruits = fruits[0:4]
print(all_fruits)
middle_two = fruits[1:3]
print(middle_two)
reverse = fruits[::-1]
print(reverse)
every_other = fruits[::2]
print(every_other)

# Modification
fruits[0] = 'avocado'
print(fruits)

# Checks
does_orange_exist = 'orange' in fruits
print(does_orange_exist)

# Append
fruits.append('lemon')
fruits.append('apple')
print(fruits)
print('apple' in fruits)

fruits.insert(2, 'lime')
print(fruits)
fruits.remove('lemon')
print(fruits)
fruits.pop(0)
print(fruits)
del fruits[1:3]
print(fruits)

# Cannot copy a list by lst1 = lst2 because then they are in the same place in memory
fruit_copy = fruits.copy()
print(fruit_copy)

# Joining lists by using +, extend is like append but for a whole list, 
vegetables = ['lettuce', 'sprouts', 'beans']
fruits.extend(vegetables)
print('Fruit and vegetables: ', fruits)

# Count
print(fruits.count('beans'))
fruits.sort()
print(fruits)

list_items = ['item1', 'item3', 'item2']
list_items.sort(reverse=True)
print(list_items)