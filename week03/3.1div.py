# 3.1div.py
# Lab 3.1 ; Program that reads in two numbers and divides the first one by the second to provide
# an integer result and the remainder
# Author: Charles Barlow

x = int(input("Enter first number: "))
y = int(input("Enter the number you want to divide by: "))
answer = int(x//y) # // gives the int division
remainder = (x%y) # % gives the remainder

print("{} divided by {} is {} with remainder {}".format(x, y, answer, remainder))