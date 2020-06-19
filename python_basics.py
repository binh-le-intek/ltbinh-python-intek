import math

def hello(name):
    correct_name = " ".join(name.split())
    welcome_message = 'Hello ' + correct_name + '!'
    return welcome_message

def calculate_hypotenuse(a, b):
    c = math.sqrt(a**2 + b**2)
    return c

def are_all_conditions_true(conditions):
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
    min_daily_rate = 0
    min_hotel = []

    for hotel in hotel_daily_rates:
        if hotel[1] < maximum_daily_rate:
            min_hotel.append(hotel[0])

    return min_hotel




