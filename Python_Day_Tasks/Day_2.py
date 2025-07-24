# [One]
# Overwrite the value of one of your variables which stores a number
# Check the id() of the variable before and after you overwrite the variable with a new number
# Why does the 'id' of the variable change?

# a=4
# print(id(a), 'ID Before')
# a=6
# print(id(a), 'ID After')

# [Two]
# Assign one variable to another
# Start with this code:
# x = 10
# y = x
# Check the id of x and y
# Explain why the id of x and y are the same
# What happens if after assigning x = y,
# I give x a different value? Does the id of y change also?

# x=50
# y=x
# print(id(x), 'ID x')
# print(id(y), 'ID y')
# Because we said x=y
# No it won't change as we still have x=y

# [Three]
# Ask the user for some input and print
# the input to the screen
# Get the user's name and print to the screen
# Improve previous code to: Get name, age and DOB details
# from a user and print the details to the screen
# a= input("What's your Date Of Birth?")
# b= input("What's your Name?")
# c= input("What's your Age")
# print ('The date of birth is' + ' ' + a + ' ' + 'and his name is' +' '+ b + ' ' + 'with an age of'+ ' ' +c)

# [Four]
# If time, improve previous code to:
# Prompt the user and get the input on the same line
# Print "Hi" on the one line
# print("Hi")
# userinput = input("Enter your Name, Date of Birth in form N/N/N and your age? ") # Added a space after the question mark for better UX
#
# split = userinput.split(",")
# #search for comma
#
# if len(split) == 3:
#     print(split[0].strip())
#     print(split[1].strip())
#     print(split[2].strip())
#
#     # convert everything back into a string
#
# else:
#     print("Invalid input")
# #
# # [Five first way]
# bad_string = 'I said \'wow\''
# print(bad_string)

# [Five two way]
# bad_string = 'I said wow'
# a = bad_string.split(" ")
# if len(a) == 3:
#     wordone = a[0].strip()
#     wordtwo = a[1].strip()
#     wordthree = a[2].strip()
# else:
#     print("Invalid input")
#
# print(wordone + " " + wordtwo + " " + "\"" + wordthree+ "\"")

# # [Five third way]
# bad_string = "I said 'wow'"
# print(bad_string)

# # [Way six]
# Hw = "Hello world!"
# print(Hw)
# print(len(Hw))
# print(Hw[0])
# print(Hw[-1])
# print(Hw[-2])
#
# # Write a comment to EXPLAIN what does this do
# print(Hw[2:])
# # gives us everything after and including the 3rd character
#
# # Write a comment to EXPLAIN what does this do
# print(Hw[-3:])
# # gives us everything after and including the 3rd last character
#
# # Write a comment to EXPLAIN what does this do
# print(Hw[:5])
# # gives everything from the start to the fifth character
# # Starts from the second, stops at the fifth (doesn't include it)
# print(Hw[1:4])

# [Way Seven]
# Summary
# Write a Python script to calculate the user's year of birth
# The task
# First part
# define the variables age_int and name_str (set dummy/default/initial values)
# make a calculation for the year in which the person was born
# print out "OMG , you are years old so you were born in " with the correct values

# age_int=22
# name_str= "Abubaker"
# year_born= 2025 - age_int
# print("You" + ' ' + name_str +' ' +"born in" ,year_born)

# Second Part
# •	prompt the user for inputs and assign the variable age_int and name_str
# •	remove the initial values set

# del age_int
# del name_str
#
# age_int = input("Enter your age: ")
# name_str= input("Enter your name: ")

# Third Part
# 	calculate and print out the total number of hours this person has lived

from datetime import datetime

now = datetime.now()
birthyear = input("Year of birth?")
birthmonth = input("Month of birth?")
birthday = input("Day of birth?")
birthdate = datetime(int(birthyear), int(birthmonth), int(birthday))

difference = now - birthdate
print("The amount of hours is", difference)