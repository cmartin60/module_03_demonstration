# for and while loops - change index to nothing
fruits = ['banana', 'pineapple', 'durian', 'apple']

for fruitElement in fruits:
    fruitElement = "Nothing"
    print(fruitElement)


# for and while loops enumerate the index
fruits = ['banana', 'pineapple', 'durian', 'apple']

for index, element in enumerate(fruits):
    print(index)

# for and while loops - print index and list and remove something from list
fruits = ['banana', 'pineapple', 'durian', 'apple']

for index, element in enumerate(fruits):
    print(index)
    if element == "durian":
        fruits.pop(index)
        
    print(element)


# for and while loops enumerate the index
fruits = ['banana', 'pineapple', 'durian', 'apple']

fruitsCopy = fruits.copy()

for f in fruits:
    print(f)

print(fruits)

"""
numbered for loop with range / !!INFINITE LOOP DONT RUN!!

for num in range(10): 
    print(num)

isTrue = True

while isTrue:
    print("it's true!")
"""

# numbered for and while
for num in range(10): 
    print(num)

user_input = int(input("Enter a number greater than ten"))

while user_input <= 10:
    print("Sorry, try that again")
    user_input = int(input())
print("great job!")



# Iterator
iterator = 0
colours = ["red", "green", "green", "yellow", "orange"]

# search list until we get a yellow value
found_colour = colours[iterator]

while found_colour != "yellow":
    iterator += 1
    found_colour = colours[iterator]

print(f"Colour found at index {iterator}")

# Iterator
iterator = 0
colours = ["red", "green", "green", "yellow", "orange"]

# search list until we get a yellow value
found_colour = colours[iterator]

while found_colour != "yellow" and iterator < len(colours):
    found_colour = colours[iterator]
    iterator += 1

print(f"Colour found at index {iterator}")

# CONTROL STATEMENTS
# iterate over number 1 to 9
# skip multiples of 3
for i in range(1,10):
    if i % 3 == 0:
        continue 
    # continue iteration until it reaches the range and/or conditions are met
    else:
        print(i)


for i in range(1,10):
    if i == 5:
        break # stops iteration after the argument is met
    else:
        print(i)


# NESTED LOOPS
letters = ['a', 'b', 'c', 'd', 'e']

for i in range (10):
    print(i)

    for j in letters:
        print(j)

first = ["dog", "cat", "mouse"]
second = ["squirrel", "mouse", "pigeon"]

for a in first:
    for b in second:
        if (a==b):
            print("matching")