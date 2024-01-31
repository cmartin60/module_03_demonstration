"""
Description: Module 03 - Introduction to Python Control Structure
Author: Christian Jorge R. Martin
Date: 30 January 2024
Usage: Demonstrate content from Module 03
"""

# Sequential, Selection, Iteration

# SELECTION
# Conditionals
# If something is the case, do one thing, otherwisem do another thing

# assignment of value
age = 20

# comparison evaluation
if age == 0:
    print("Not born yet")
    print("This is a weird way to indicate that")
    print("Why are you still here?")
elif age < 13: # "else if" (evaluate this if the previous evaluation was false)
    print("Child")
else:
    print("None of the specified ages")

if True:
    print("It's true")

# if (value that is true):
#      run code
if False:
    print("It's not true")

# Nested Conditionals
    
x_pos = 0
y_pos = 0

y_sign = ""
x_sign = ""

if x_pos > 0:
    x_sign = "positive"
elif x_pos < 0:
    x_sign = "negative"
else:
    x_sign = "zero"

if y_pos > 0:
    y_sign = "positive"
elif y_pos < 0:
    y_sign = "negative"
else:
    y_sign = "zero"

print(f"X is {x_sign} and Y is {y_sign}")

# == Equality (0 == 0 = True - checks if the value are the same)
# ! isNOT operator ( 0 != 1 = True)

if x_pos != y_pos:
    print("x and y positions are not equal")

# LOGICAL OPERATORS: and, or, not
    
if x_pos > y_pos and y_pos > 0 and y_pos == 0 and y_pos < 0:
    print("X is greater than y -- y is greater than zero")

# this will always evaluate to true
if x_pos == 0:
    if (y_pos > 0 or y_pos < 0):
        print("X zero or Y us not zero")

# Ternary expressions
my_num = 12
if my_num % 2 == 0:
    print("even")
else: 
    print("odd")

#ternary: assign the value of "result" based on the conditional
result = "even" if my_num % 2 == 0 else "odd"

# in
fruits = ['apple', 'banana', 'kiwi', '3']

print('banana' in fruits) #output true
print(3 in fruits) #output false , 3 is int 

sentence = "this was sent."
print("sent " in sentence) #output false due to space