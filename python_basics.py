import math

def hello(name):
    correctName = " ".join(name.split())
    welcomeMessage = 'Hello ' + correctName + '!'
    return welcomeMessage

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
