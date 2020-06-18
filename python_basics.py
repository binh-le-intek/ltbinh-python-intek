import math

def hello(name):
    correctName = " ".join(name.split())
    welcomeMessage = 'Hello ' + correctName + '!'
    return welcomeMessage

def calculate_hypotenuse(a, b):
    c = math.sqrt(a**2 + b**2)
    return c
