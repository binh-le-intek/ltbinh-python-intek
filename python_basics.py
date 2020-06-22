import math
import re
import time
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

def hello(name):
    if type(name) != str:
        raise TypeError("Not a string")
    correct_name = name.strip()
    if len(correct_name) == 0 or len(correct_name) >= 20:
        raise ValueError("Not a valid string")
    welcome_message = 'Hello ' + correct_name + '!'
    return welcome_message

def calculate_hypotenuse(a, b):
    c = math.sqrt(a**2 + b**2)
    return c

def are_all_conditions_true(conditions):
    if type(conditions) == type(None):
        return conditions
    if len(conditions) == 0:
        return None
    
    for x in conditions:
        if x == False:
            return False
    return True

def is_a_condition_true(conditions):
    if len(conditions) == 0:
        return None
    for x in conditions:
        if x == True:
            return True
    return False

def filter_integers_greater_than(l, n):
    filter_list = []
    for x in l:
        if x>n:
            filter_list.append(x)
    return filter_list

def find_cheapest_hotels(hotel_daily_rates, maximum_daily_rate):
    min_hotel = []

    for hotel in hotel_daily_rates:
        if hotel[1] <= maximum_daily_rate:
            min_hotel.append(hotel)

    min_hotel = sorted(min_hotel, key=lambda item:item[1])
    value = []
    for i in range(len(min_hotel)):
        value.append(min_hotel[i][0])

    return value

def calculate_euclidean_distance_between_2_points(p1, p2):
    euclidean_distance = math.sqrt((p1[0]-p2[0])**2 +(p1[1]-p2[1])**2)
    return euclidean_distance

def calculate_euclidean_distance_between_points(points):
    if len(points)<2:
        raise ValueError('The list MUST contain at least 2 points')

    sum_length = 0
    for i in range(len(points) - 1):
        j = i + 1
        sum_length += calculate_euclidean_distance_between_2_points(points[i], points[j])

    return sum_length

def capitalize_words(s):
    if type(s) == type(None):
        return None
    if type(s) != str:
        raise TypeError("Not a string")
    
    s = s.lower()
    s = s.split() 
    new_string = [] 

    for i in range(len(s)):
        word = s[i][0].upper() + s[i][1:]
        new_string.append(word)

    return " ".join(new_string)

def uppercase_lowercase_words(s):
    if type(s) == type(None):
        return None
    if type(s) != str:
        raise TypeError("Not a string")

    s = s.split()
    for i in range(len(s)):
        if i%2==0:
            s[i] = s[i].upper()
        else:
            s[i] = s[i].lower()
    return " ".join(s)

def factorial(n):
    if type(n) != int:
        raise TypeError("Not an integer")
    elif n<0:
        raise ValueError("Not a positive integer")

    if n == 0 or n == 1:
        return 1
    
    return n*factorial(n-1)

def char_to_int(c):
    if type(c) != str:
        raise TypeError("Not a string")
    elif len(c) > 1:
        raise ValueError("Not a single digit")

    value = ord(c)
    if (value < 48 or value > 57):
        raise ValueError("Not a positive integer string expression")    

    return value - 48

def string_to_int(s):
    if type(s) != str:
        raise TypeError("Not a string")

    value = 0
    for i in range(len(s)):
        value += char_to_int(s[i])
        value *= 10
    value //= 10
    return value

def is_palindrome(value):
    if type(value) == type(None):
        return False

    value = str(value)
    value = ("".join(re.split('\W', value))).lower()
    if len(value) == 0:
        return False
    
    if len(value) % 2 == 0:
        count = len(value)//2
    else:
        count = len(value)//2 - 1

    for i in range(count):
        if value[i] != value[-i-1]:
            return False

    return True


def roman_numeral_to_int(roman_numeral):
    if not(isinstance(roman_numeral, str)) or len(roman_numeral) == 0:
        raise TypeError("Not a string")
    roman_list = {
            'N': 0,
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
    }
    for i in range(len(roman_numeral)):
        if roman_list.get(roman_numeral[i]) == None:
            raise ValueError("Not a Roman numeral")
    count = 1
    for i in range(len(roman_numeral)-1):
        if roman_numeral[i] == roman_numeral[i+1]:
            count += 1
        else:
            count = 1
        if count == 4:
            raise ValueError("Not a Roman numeral")
    
    
    value = 0
    i = 0
    while i < len(roman_numeral) - 1:
        s1 = roman_list[roman_numeral[i]]
        s2 = roman_list[roman_numeral[i+1]]
        if s1 >= s2:
            if (s1 + s2) == 10 or (s1+s2) == 100 or (s1+s2) == 1000:
                raise ValueError("Not a Roman numeral")
            value += s1
        else:
            minus = s2 - s1
            if minus == 4 or minus == 9 or minus == 40 or minus == 90 or minus == 400 or minus == 900: 
                i += 1
                value = value + minus
            else:
                raise ValueError("Not a Roman numeral")
        i += 1

    if i == len(roman_numeral) - 1:
        value += roman_list[roman_numeral[i]]

    return value

def play_melody(melody, sound_basedir):
    if not(isinstance(melody, list) or isinstance(melody, tuple)) or len(melody) <= 1:
        raise TypeError("Not a string")
    for i in range(len(melody)):
        if not(isinstance(melody[i], str)):
            raise TypeError("Not a string")

    for i in range(len(melody)):
        if len(melody[i]) <= 1 or len(melody[i]) > 3:
            raise ValueError("Not a valid melody")
        available_melody = ['A', 'B', 'C' , 'D', 'E', 'F', 'G']
        if melody[i][0] not in available_melody:
            raise ValueError("Not a valid melody")
        if len(melody[i]) == 2:
            if int(melody[i][1]) < 2 or int(melody[i][1]) > 5:
                raise ValueError("Not a valid melody")
        else:
            if melody[i][1] != 'B' and melody[i][1] != '#':
                raise ValueError("Not a valid melody")
            if int(melody[i][2]) < 2 or int(melody[i][2]) > 5:
                raise ValueError("Not a valid melody")
            if (melody[i][0] == 'E' and melody[i][1] == '#') or (melody[i][0] == 'F' and melody[i][1] == 'B') or (melody[i][0] == 'B' and melody[i][1] == '#') or (melody[i][0] == 'C' and melody[i][1] == 'B'):
                raise ValueError("Not a valid melody")

    pygame.mixer.init()
    list_sound = []
    for i in range(len(melody)):
        cur_melody =  melody[i].lower()
        if  cur_melody[1] == '#':
            cur_melody = list(cur_melody)
            cur_melody[1] = 'b'
            if  cur_melody[0] == 'c':
                cur_melody[0] = 'd'
            elif  cur_melody[0] == 'd':
                cur_melody[0] = 'e'
            elif  cur_melody[0] == 'e':
                cur_melody[0] = 'f'
            elif  cur_melody[0] == 'f':
                cur_melody[0] = 'g'
            elif  cur_melody[0] == 'g':
                cur_melody[0] = 'a'
            elif  cur_melody[0] == 'a':
                cur_melody[0] = 'b'
            elif  cur_melody[0] == 'b':
                cur_melody[0] = 'c'
                cur_melody[2] = str(int(cur_melody[2])+1)
            cur_melody = ''.join(cur_melody)
        cur_sound = sound_basedir + '/' +   cur_melody + '.ogg'
        list_sound.append(cur_sound)
        sound = pygame.mixer.Sound(cur_sound)
        sound.play()
        time.sleep(0.4)
        #pygame.time,delay(400)
        

    return list_sound

print(roman_numeral_to_int('IXC'))