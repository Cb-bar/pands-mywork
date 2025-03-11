# 3.2floor.py
# Lab 3.2 ; This program takes in a float and outputs an int that is rounded down
# Author: Charles Barlow

import math

numberTofloor = float(input("Enter a float number: "))
flooredNumber = math.floor(numberTofloor)
print('{} floored is {}'.format(numberTofloor, flooredNumber))