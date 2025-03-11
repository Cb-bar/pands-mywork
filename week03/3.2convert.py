# 3.2convert.py
# Lab 3.2 ; This program takes in a float amount of dollars and returns that absolute amount in cent.
# Author: Charles Barlow
# Citation for work: 

import math


number = float(input("Enter a dollar amount: $ "))
finalNumber = abs(number)
print('The value of ${} in cents is {}'.format(number, finalNumber))