import string
import random

def random_user_id(length):
    character_number_string = string.ascii_lowercase + string.digits
    j = 0
    userID = ""
    while j < length:
        index = random.randint(0, len(character_number_string)-1)
        userID += character_number_string[index]
        j += 1
    return userID

def user_id_gen_by_user():
    num_characters = int(input("Enter the desired number of characters: "))
    quantity = int(input("Enter the desired number of user IDs: "))
    for _ in range(quantity):
        print(random_user_id(num_characters))

def rgb_color_gen():
    quantity_red = random.randint(0,255)
    quantity_green = random.randint(0,255)
    quantity_blue = random.randint(0,255)
    return "rgb(" + str(quantity_red) + "," + str(quantity_green) + "," + str(quantity_blue) + ")"
    
def list_of_hexa_colors(number_of_strings):
    hexadecimal = string.ascii_lowercase[0:5] + string.digits
    hexadecimal_array = list()
    for _ in range(number_of_strings):
        hexadecimal_array.append("#" + "".join(random.choices(hexadecimal, k = 6)))
    return hexadecimal_array

def list_of_rgb_colors(number_of_rgb):
    rgb_colors = list()
    for _ in range(number_of_rgb):
        rgb_colors.append(rgb_color_gen())
    return rgb_colors

def generate_colors(type, number):
    color_list = list()
    if type == 'hexa':
        color_list = list_of_hexa_colors(number)
    elif type == 'rgb':
        color_list = list_of_rgb_colors(number)
    else:
        color_list = None
    return color_list

def shuffle_list(list_1):
    random.shuffle(list_1)
    return list_1
    
def random_7_numbers():
    array_of_7 = list()
    while len(array_of_7) < 7:
        random_int = random.randint(0,9)
        if random_int in array_of_7:
            continue
        else:
            array_of_7.append(random_int)
    return array_of_7