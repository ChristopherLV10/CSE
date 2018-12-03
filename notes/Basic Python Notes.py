"""
print("Hello World")

# This is a comment. This has no effect on the code
# but this does allow me to do things. I can:
# 1. Make notes to myself
# 2. Comment pieces of code that do not work
# 3. Make my code easier to read

print("Look at what happens here. Is there any space?")
print()
print()
print("There should be a couple blank lines here")

# Math
print(3 + 5)
print(5 - 2)
print(3 * 4)
print(6 / 2)

print("Figure this out...")
print(6 // 2)
print(5 // 2)
print(9 // 4)

print("Here is another one...")
print(6 % 2)
print(5 % 2)
print(11 % 4)  # Modulus (Remainder)

# Powers
# What is 2^20
print(2 ** 100)

# Taking input
name = input("What is your name?")
print("Hello %s." % name)

age = input("How old are you? >_")
print("%s?!? You belong in a museum." % age)
print()
print("%s is really old. They are %s years old." % (name, age))

# Variable Assignments
car_name = "Wiebe Mobile"
car_type = "Tesla"
car_cylinders = 16
car_miles_per_gallon = 0.01

# Make it print "I have a car called Wiebe Mobile. It is a Tesla."
print("I have a car called %s. It is a %s" % (car_name, car_type))

# Recasting
real_age = int(input("How old are you again?")
hidden_age = real_age + 5
print("This is your real age: %d"% hidden_age)
"""

"""
This is a multi-line comment
Anything between the "s is not run
"""


# Functions
def say_it():
    print("Hello World!")


say_it()
say_it()
say_it()


# f(x) = 2x + 3
def f(x):
    print(2*x + 3)


f(1)
f(5)
f(5000)


# Distance Formula
def distance(x1, y1, x2, y2):
    dist = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
    print(dist)


distance(0, 0, 3, 4)
distance(0, 0, 5, 12)

# Loops
for i in range(10):   # This gives the numbers 0 through 4
    say_it()

for i in range(10):
    print(i + 1)

for i in range(5):
    f(i)

# While loops
a = 1
while a < 10:
    print(a)
    a += 2    # This is the same as saying a = a + 1


"""
At the moment you start the loop:
For loops - Use when you know EXACTLY how many iterations
While loops - Use when you DON'T know how many iterations
"""

# Control Structure (If Statements)
sunny = True
if sunny:
    print("Go outside")


def grade_calc(percentage):
    if percentage >= 90:
        return"A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return"F"


your_grade = grade_calc(82)
print(your_grade)

# "Random" Notes
import random  # This should be on line 1
print(random.randint(0,100))



# Creating a list
colors = ["blue", "turquoise", "pink", "orange", "black", "red", "brown", "white", "purple"]  #USE SQUARE BRACKETS!!!!
print(colors)
print(colors[1])
print(colors[0])

# Length of the list
print("There are %d things in the list." % len(colors))
# Changing Elements in a list
colors[1] = "Green"
print(colors)

# Looping through lists
for item in colors:
    print(item)

'''
1. Make a list with 7 items
2. change the third thing in the list
3. print the item
4. print the full list
'''
new_list = ["United States", "Mexico", "Canada", "France", "Germany","Spain", "Argentina"]
new_list[2] = "Columbia"
print(new_list[2])
print(new_list)
print("The last thing in the list is %s" % new_list[len(new_list) - 1])



food_list = ["Pie", "Tamales", "Pizza", "chicken", "burrito", "sushi", "chips", "Hot wings", "soup", "Hamburger"
             , "Bacon", "tacos", "salmon", "carne asada", "flan", "chili", "noodles", "eggs","waffle", "salad"]
print(len(food_list))


# Adding stuff to a list
food_list. append(".")
food_list. append(";")

print(food_list)

food_list.insert(1,"eggo waffles")
print(food_list)

# Removing things from a list
food_list.remove("salad")
print(food_list)
print()
print()
new_list2 = ["Dog", "Cat","Fish"]
new_list2.insert(3, "Bear")
print(new_list2)
new_list2.remove("Cat")

print(new_list2)

# Tuples
brands = ("apple", "samsung", "HTC")    # Notice these have parentheses

# Also removing stuff from a list
print(food_list)
food_list.pop(0)
print(food_list)


# Find the index of and item
print(food_list.index("chicken"))

# Changing things into a list
string1= "turquoise"
list1 = list(string1)
print(list1)

# Turn a list into a string
print("".join(list1))



# Hangman hints
for i in range(len(list1)): # i goes through all indicies
    if list1[i] == "u": # if we find a U
        list1.pop(i)    # remove the i-th index
        list1.insert(i, "*")    # Put a * there instead

# Turn a list into a string
print("".join(list1))

'''
for character in list1:
if character == "u":
# replace with a *
current_index = list1.index(character)
list1.pop(current_index)
list1.insert(current_index,"*")


'''

# Function Notes
# a**2 + b**2 = c**2


def pythagorean(a, b):
    return (a**2 + b**2)**(1/2)


print(pythagorean(3, 4))

