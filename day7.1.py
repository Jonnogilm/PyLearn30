# unorderd and un-indexed distinct elements
# can find union(everything from both sets) intersection(everything from both) difference(in one but not the other) symmetric difference(in one or other but not both) subset(everything in one set is in the other) superset(one set contains all the other) disjoint is none in common

fruits = {'banana', 'orange', 'mango', 'lemon'}
print(len(fruits))
print('mango' in fruits)
fruits.add('pinapple')
print(fruits)
fruits.update({'kiwi', 'strawberry', 'blueberry'}) # can add a list, tuple, or set
print(len(fruits))
print(fruits)
fruits.discard('dragonfruit')
fruits.remove('mango')
removed_fruit = fruits.pop()
print(fruits)
print(removed_fruit)

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.difference(st1))
print(st1.difference(st2)) 