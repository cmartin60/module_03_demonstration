# Import 
import math
from math import sqrt
import random


radius = 3

# qualifications of the PI Constant
area = math.pi * radius ** 2
print(area)

square = 16

# sqrt is "fully qualified" already
root = math.sqrt(square)

# print a random number
print(random.random())

# print random int 1-6
print(random.randint(1,6))

# print a random from a list
fruits = ['banana', 'apple', 'durian']

print(random.choice(fruits))

# modified the list and shuffled it (other way)
fruits = ['banana', 'apple', 'durian']
random.shuffle(fruits)

print(fruits)

#write an algorithm that removes all of the odd number from a list
nums = [1, 2, 6, 7, 4, 9, 10]

# remove numbers at a random, and if you ever remove an even one try again
nums.pop(random.randint(0, len(nums)))

# File Input and Output
# Sending and receiving information from outside of the program 
# file can be opened or closed 

# r = "read" file
# file = open (r"./example.txt", "r")
# content = file.read()
# print(content)
# file.close()

# with clause
with open(r"example.txt", "r") as file:
    content = file.read()

print(content)

with open(r"dict_example.txt", "r") as dict_input:
    for line in dict_input:
        print(line)