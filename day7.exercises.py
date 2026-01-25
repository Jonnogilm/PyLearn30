# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add('Twitter')
it_companies.update({'Shopify', 'Stripe', 'More'})
print(it_companies)
it_companies.remove('More')

# Remove throws an error when it doesn't see the string it is looking for while discard does not

C = A.union(B)
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))

A.update(B)
B.update(A)

print(A.symmetric_difference(B))
del A
del B

ages_set = set(age)
print(len(ages_set) > len(age))
print(len(ages_set) < len(age))
print(len(ages_set) == len(age))

# 2. String can only hold a single thing of string data, lists are mutable and indexed, tuples are indexed but not mutable, sets are mutable but they are not indexed
sentance = 'I am a teacher and I love to inspire and teach people'
words = sentance.split(' ')
words_set = set(words)
print('There are', len(words_set), 'unique words in the sentance.')