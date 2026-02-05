# use else to run a block when the condition is no longer true. But doesnt it continue anyway so it is redundant
# actually used to because when it breaks and doesn't complete the loop it does not run the else:
# if another_condition: break
# if another_condition: continue --> break the current iteration and continue with the next

count = 0
even_numbers = list()

while count < 10:
    count += 1
    if count%2 == 0:
        even_numbers.append(count)
        continue
    print(count)
    
else:
    print("The last number is not odd. I have succesfully completed the loop.")

# for loops are for iterating over a sequence: means lists, tuples, sets, strings, dictionaries
# closer to an enhanced for loop in java than a regular one
numbers = even_numbers.copy()

for number in numbers:
    print(number)

# Looping through a dictionary gives you the keys so you would then need to do print(person['iterator'])
# or pass two iterables so for key, value in person.items()
# can also use breaks for for loops --> so does the function of a non-enhanced for loop?
# also can use continue so like i+=2
# range returns a list of numbers range(start, end, step) default is starts at 0 and increment is 1

for number in range(2, 20, 2):
    print(number)

# nested for loops exist and so does else(not run if there is a 'break' )
# use pass if there is a required statement but you do not want anything to be executed there