#A function that takes a number and return the squareroot if it is divisible by 5 and reminder if it is not.
import math
def divide_or_square (number):
    if number % 5 == 0:
        return  math.sqrt(number)
    else:
        return number % 5