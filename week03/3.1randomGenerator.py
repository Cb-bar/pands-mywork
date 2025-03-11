# 3.1randomGenerator.py
# Lab 3.1 ; Program that prints out a random number between 1 and 10.
# Author: Charles Barlow

import random

# First part of task below
# number = random.randrange(1,10)
# print("Here is a random number {}".format(number))

# Second 'extra' part of task below where the user can input the range 
# and a random number is picked from that range

number1 = int(input("Enter First Number of Range: "))
number2 = int(input("Enter Second Number of Range: "))
answer = random.randint(number1, number2)
print("Here is a random number from the range you provided {}".format(answer))

