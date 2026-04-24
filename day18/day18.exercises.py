import re

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
lst_of_words = re.findall(r'[a-zA-Z]+', paragraph)
# print(lst_of_words)

count_words = {}
for word in lst_of_words:
    if word in count_words:
        count_words[word] += 1
    else:
        count_words.setdefault(word, 1)
print(count_words)


txt = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.'

# Extract these numbers from this whole text and find the distance between the two furthest particles.
numbers = re.findall(r'[-]\d+', txt)
numbers_num = [int(number) for number in numbers]
print(numbers_num)

differences = []
for x in numbers_num:
    for other_num in numbers_num:
        differences.append(abs(x - other_num))
differences_high_low = sorted(differences, reverse=True)
print(f"Highest distance is {differences_high_low[0]}")



