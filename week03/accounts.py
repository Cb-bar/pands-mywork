# accounts.py
# Lab 3.3 ; This program reads in a 10 character account number 
# and outputs the account number with only the last 4 digits showing
# Author: Charles Barlow


accountNumber = input("Please enter a 10 digit account number: ")

# For account number with X showing + final 4 digit. I am going to concatenate two string.
# Source: https://www.w3schools.com/python/python_strings_concatenate.asp
# Additionally, going to slice the string to return only the final 4 digits.
# Source: https://www.w3schools.com/python/python_strings_slicing.asp

hiddenAccountNumber = 'XXXXXX' + accountNumber[-4:]
print(hiddenAccountNumber)

# Extra: Modify the program to deal with account numbers of any length

## extraAccountNumber = accountNumber[-4:]
## lengthOfAccountNumber = len(accountNumber)
