# 3.3normalise.py
# Lab 3.3 ; This program reads in a string and strips any leading or trailing spaces
# and converts the string to lower case
# Author: Charles Barlow

rawString = input("Please enter a string: ")
normalisedString = rawString.strip().lower()

lengthOfRawString = len(rawString)
lengthOfNormalised = len(normalisedString)

print(f"That string normalised is: {normalisedString}")
print(f"we reduced the input string from {lengthOfRawString} to {lengthOfNormalised} characters")