import math

def hello(name):
    correctName = " ".join(name.split())
    print('Hello ' + correctName + '!')

def calculate_hypotenuse(a, b):
    c = math.sqrt(a**2 + b**2)
    print(c)


