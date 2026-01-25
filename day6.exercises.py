empty_tpl = ()
tpl_brothers = ('Kirk', 'Andrew', 'Ben', 'Bruno')
tpl_sisters = ('Clarissa', 'Hermione', 'Holly')
tpl_siblings = tpl_brothers + tpl_sisters
print(tpl_siblings)
print('I have', len(tpl_siblings), 'siblings')

temp = list(tpl_siblings)
temp.extend(['Mark', 'Susan'])
family_members = tuple(temp)
print(family_members)

*siblings, father, mother = family_members
print(siblings)
print(mother)
print(father)

fruits = ('apple', 'banana', 'orange', 'kiwi')
vegetables = ('carrot', 'lettuce', 'pepper')
animal_products = ('milk', 'eggs', 'chicken')

food_stuff_tp = fruits+vegetables+animal_products
food_stuff_lt = list(food_stuff_tp)
middle_item = food_stuff_lt[len(food_stuff_lt)//2]
first_three = food_stuff_lt[0:3]
last_three = food_stuff_tp[-3:]
print(first_three)
print(last_three)

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
