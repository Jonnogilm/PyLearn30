numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered_nums = [i for i in numbers if i <= 0]
print(filtered_nums)

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list)

tuple_list = [(x, 1, x, x * x, x ** 3, x ** 4, x ** 5) for x in range(11)]
print(tuple_list)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_countries = [country for row in countries for country in row]
rewrite_countries = [list(tuple) for tuple in flattened_countries]
print(rewrite_countries)
for list in rewrite_countries:
    for country in list:
        list[list.index(country)] = country.upper()
    list.insert(1, list[1][0:3])
print(rewrite_countries)
    
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
dict_locations = [{'country': country, 'city': city} for list in countries for country, city in list]
print(dict_locations)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
full_names = [firstname + " " + lastname for inner_list in names for firstname, lastname in inner_list]
print(full_names)

def find_slope():
    return lambda x1, y1, x2, y2: (y2-y1)/(x2-x1)

print(find_slope()(1, 3, 4, 5))
y_intercept = lambda x, y, m: y - m * x
print(y_intercept(1,4,7))