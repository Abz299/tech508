# Day 4
# Topic: Functions
# Group task: Make functions
# Note: This will be given to you when your group is assigned this task.
#
# 🎯 Outcome (By doing this you should): Learn how to use functions to re-use code when whenever it is needed.
# 🎥 For an introduction, please watch "Functions Introduction" on the Sparta Global "Python Fundamentals" Teachable course: https://sparta-academy.teachable.com/courses/python-fundamentals/lectures/31831939

# 1.	Make a function with no argument
    # a.	Name it 'print_something' and all it should do it print something to the screen
    # b.	Call the function to test it works

# Define a function named 'print_something' that takes no arguments.
def print_something():
    print("Check1 'print_something'")
print_something() #calling of the function

# 2.	Make a function with one argument
    # a.	Aim: Improve the last function by having it receive an argument to replace the 'hard coded' string
    # b.	Make a new improved function which
    # i.	Accepts a string variable as an argument
    # ii.	Prints the string variable received as an argument

def print_something_2(greeting):
    print(greeting)
print_something_2("check2")

# 3.	Make a more interesting version of a function that accepts one argument
# a.	Here is the code to call the function:
#
# greet("Susan")
#
# b.	You need to write the function
# c.	Make sure the print statement in your function uses concatentation (ie. +) rather than an f-string
# d.	Output should be:
#
# Hello, my name is Susan.
#
def greeting(name):
    print("Hello, my name is " + name + ".")

greeting("susan")

# 4.	Make a function with 2 arguments that returns a value
# a.	Troubleshoot this code so that the function returns the correct value of 4:def addition(int1, int2):
#     int1 + int2
#
# print(addition(2, 2))
#
# b.	This time we do NOT want the function to do the print to the screen
# c.	Document what you've learnt

def addition(int1, int2):
    print(int1 + int2)

addition(1, 2)

# 5.	Make a function with default values
# a.	Copy your working code from the last exercise (that adds 2 and 2 together) as starting code for this exercise
# b.	Replace line of code to call the function with this:
#
# print(addition())
#
# c.	Run your code - you should get an error
# d.	Modify your function so that int1 and int2 both have the default value of 2
# e.	Run your code and make sure the result is 4
# f.	Now call your function with this line of code:

# def addition(int1, int2):
#     print(int1 + int2)
#
# addition(2, 2)#whenever you want to call a function, only call it with its function name

# 6.	Make a function that accepts any number of arguments
# a.	Design a function called 'print_every_number' which accepts a tuple of numbers as an argument
# b.	The function should do 2 things:
# i.	Print the type of the tuple that was passed in as an arguments
# ii.	Loop through the tuple and print each item in the tuple on a separate line
# c.	After calling the function, the output should be:
# <class 'tuple'>
# 1
# 2
# 2
# 3
# 3
# 4
# 5
# 5
#
# d.	Explain what character allows your function to accept multiple arguments

# def print_every_number(fruits):
#     print(fruits)
#
# fruitsbuy = ("apple","banana","pear","strawberry","grapes")
#
# for fruitlist in fruitsbuy:
#
#     print_every_number(fruitlist)

# 7.	Make a function which gives a hint about an argument's data type
# a.	Some people think stricter typing should be used with Python as best practice, let's find out why
# b.	See what happens if you call your earlier greet function with this line of code:
# greeting(24601) #data type much remain as string not an integer
#
# c.	To HELP us avoid this type of error, define the type of argument accepted into our function so that we are given a warning BEFORE we even run our Python script:
#str()
# i.	Define that data type accepted by your greet function is a string
# ii.	Notice that PyCharm now gives the warning Expected type 'str', got 'int' instead BEFORE you even run your code

