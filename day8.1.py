# unordered, mutable, paired (key: value)
# create with curly brackets or dict()
# can have multiple different types of data kept within

dit1 = {
    'first_name' : 'Jonno',
    'age' : 18,
    'country' : 'USA'
}
print(dit1)

#len() shows amt of key:value pairs
print(len(dit1))

#access items by their keys, if not found it raises an error. Use .get() method to get around this error
print(dit1['age'])
print(dit1.get('country'))
print(dit1.get('city'))

#add new keys
dit1['street'] = 'Washington'

#use in operator to check if a certain key is in the dictionary
print('street' in dit1)
print('city' in dit1)

removed = dit1.pop('street')
print(removed)

del removed

#items() changes dicts into a list of tuples
# print(dit1.items())

#use clear(), del, copy() as normal
#keys() method returns all the keys
#values() method returns all the values
print(dit1.keys())
print(dit1.values())
