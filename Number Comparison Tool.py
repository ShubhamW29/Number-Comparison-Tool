# PROGRAM: Number Comparison Tool
# DESCRIPTION:
# This simple Python program compares two numbers entered by the user
# and tells whether 'a' is greater than 'b', 'b' is greater than 'a', or both are equal.

print("Welcome to the Number Comparison Tool")
print("------------------------------------------------")

a = int(input("Enter the number 1: "))
b = int(input("Enter the number 2: "))

if a > b: print("a is greater than b: ") # a is greater than b

elif a < b: print("b is greater than a: ") # b is greater than a

else:print("a is equal to b: ") # a is equal to b

print("------------------------------------------------")
print("Thank u for using the Number Comparison Tool!")