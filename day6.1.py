# unchangable, ordered, written with round brackets, similar to final in Java
# turple(), count(), index(), + can add turples together
# Tuples are immutable but if you want to modify it you CAN change it to a list: lst = list(tpl)

tpl = (1, 2, 3, 4, 5, 6)
print(tpl)
list_tpl = list(tpl)
list_tpl.extend([7, 8, 9])
print(list_tpl)
new_tpl = tuple(list_tpl)
print(new_tpl)

print(9 in tpl)
print(9 in new_tpl)

tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2
print(tpl3)

del tpl1