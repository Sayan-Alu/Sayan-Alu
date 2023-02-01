
#   
# 
# Here's a Python program that checks if a given character is a digit or not using the isdigit() method:

'''
char = input("Enter a character: ")

if char.isdigit():
    print("The character is a digit.")
else:
    print("The character is not a digit.")'''

class DigitChecker:
    def __init__(self, string):
       self.string = string

    def check_digit(self):
        if self.string.isdigit():
            return "The string is a digit."
        else:
            return "The string is not a digit."

A = input("Enter a string: ")
checker = DigitChecker(A)
print(checker.check_digit())