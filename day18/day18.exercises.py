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

def is_valid_variable(string_to_check):
    bad_if = []
    bad_if = re.findall(r'^\d|[^a-zA-Z0-9_]', string_to_check)
    return False if len(bad_if) > 0 else True

print(is_valid_variable('first_name')) # True
print(is_valid_variable('first-name')) # False
print(is_valid_variable('1first_name')) # False
print(is_valid_variable('firstname')) # True

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean(string_to_clean):
    cleaned = re.sub(r'[^a-zA-Z ]', '', string_to_clean)
    return cleaned
cleaned_teacher_sentance = re.findall(r'[a-zA-Z]+', clean(sentence))
print(cleaned_teacher_sentance)
tracking = {}
for word in cleaned_teacher_sentance:
    if word in tracking:
        tracking[word] += 1
    else:
        tracking.setdefault(word, 1)
sorted_tracking = {key: value for key, value in sorted(tracking.items(), key=lambda item: item[1], reverse=True)[:3]}
print(sorted_tracking)
