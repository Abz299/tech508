# [Task 1]
# 1.	Create a list called 'shopping_list' with the following items:
# a.	eggs
# b.	bread
# c.	bananas
# d.	biscuits
# e.	milk
# 1.	Create a list called 'shopping_list' with the following items:
shopping_list=["Eggs", "Bread", "Bananas",
               "biscuits", "milk", "coffee"]
# 2.	Print the list to the screen
print("The shopping list is the following:", shopping_list)

# for product in shopping_list:
#     print(product)

# 3. Print the data type of 'shopping_list'
# print(type(shopping_list))

# 4.	Print the first item in the list
# print(shopping_list[0])


# 5.	Print the last item in the list
# lastword = shopping_list[-1]
# print(lastword)

# 6 Change the second item in the list (i.e. 'bread')
# to 'rice' instead, then print the second item to the screen
# to prove it's been changed

# shopping_list[1]= "rice"
# for product in shopping_list:
#     print(product)

# 7.	Use the list('s method to add the item carrots'
# to the list (you should not re-assign the list using ')='),
# then check the length of the list (which should now have 6 rather
# than 5)

# shopping_list.append('carrot')
# for product in shopping_list:
#      print(product)

# 8.	Add another list with two items ('toffee' and 'coffee') to the 'shopping_list' list. Use one of the list's methods to add the two items in one go.
# a.	Print the 'shopping_list' to check 'toffee' and 'coffee' have been added correctly.

# shopping_list.extend(["toffee","coffee"])
# for product in shopping_list:
#       print(product)

# 9.	Remove "bananas" from 'shopping_list'.
# Print 'shopping_list' to check it's been removed.

# shopping_list.remove("Bananas")
# for product in shopping_list:
#       print(product)

# 10.	Remove the last item ('coffee') from 'shopping_list'
# using the pop method.
# Check it worked by printing 'shopping_list'

# shopping_list.pop()
# for product in shopping_list:
#        print(product)

# [Task 2]
# Mix all the data about a user into a list

# 1. Use your code from the "Task:
# Python variable basics" (last subtask)
# where you asked the user for their name, age and DOB.

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# DOB = input("Enter your date of birth: ")
#
# # 2.Mix the name, age and DOB into one list user_details_list
#
# user_details_list = [name, age, DOB]
# for user_details in user_details_list:
#     print(user_details)

# 4.Check the age is saved as an integer in the list.
# If it('s not, work out how to convert it to an integer
# and add the age integer to the list.)

# print(type(age))
#
# # 5.Ask the user for their height in cm and save it
# # to the variable height
#
# variable_height= int(input("Enter your height in cm: "))
# print(type(variable_height))
#
# # 6.Save height as a float in the list,
# # and print the height from the list.
#
# variable_height= int(input("Enter your height in cm: "))
# variable_height=float(variable_height)
# print(type(variable_height))

# [Task 3]
# Task: Test you can slice lists
# outcome (By doing this you should): Learn how to slice lists
# •	You have probably already covered string slicing
# •	List slicing is similar, except we are cutting up a list
# of item rather than a string of characters

# mixture = [1, 2, 3,"one", "two", "three"]
#
# print(mixture)
# # Returns the 2nd and 3rd items in the list -> It should return [2, 3]
# print(f"{mixture [1:3]}")
# #Returns every second item in the list -> It should return [1, 3, 'two']
# print(f"{mixture [::2]}")
# # Start at the last item, stop at the 3rd last item, and step
# # in reverse order -> It should return ['three', 'two']
# print(f"{mixture [-1:-3:-1]}")


# # [Task 4]
# # Task: Learn tuples - finish the "Stranded on a Desert Island" game
# # Outcome (By doing this you should): Learn how to use tuples and how they are different to lists
#
# # "Stranded on a Desert Island" game
# # Rationale: Practice tuples
# # Type of exercise: Finish the code
# print("You are stranded on a desert island. You can take only THREE items.")
# essential_item1 = input("What is an essential item you would take one? ")
# essential_item2 = input("What is an essential item you would take two? ")
# essential_item3 = input("What is an essential item you would take three? ")
# # save the items as a tuple
# essentials_tuple =(essential_item1, essential_item2, essential_item3)
# # print the tuple
# print("Here are your items as a tuple:", essentials_tuple)
# print("")
# print("I lied. You can take one more item.")
# essential_item4 = input("What is one more essential item you would take? ")
# # try to add the 4th item to the tuple
# # if you can't add the 4th item, work out how to save the 4th item to the tuple
# essentials_tuple = essentials_tuple + (essential_item4,)
# # convert a string into a tuple put a comma at the end
# print("Here are your items as a tuple (with the 4th item added):", essentials_tuple)

# print(type(essentials_tuple))
# print(type(essential_item4))

# [Task 5]
# Task: Working with dictionaries
# 🎯 Outcome (By doing this you should): Learn how to use a dictionary
# 1.	Make a dictionary called "student_1" containing the following information:
# a.	name: susan
# b.	stream: tech
# c.	completed_lessons: 4 (should be saved as an integer not a string)
# d.	completed_lesson_names: value should be list of these 3 items: "variables", "data_types", "set up"
#
# student_1 = {
#     'name': 'susan',
#     'stream': 'tech',
#     'completed_lessons': int(4),
#     'completed_lessons_names': ["variables", "data types", "set up"]
# }

# # 3.Print the dictionary to the screen
# print(student_1)
# # 4.Print its data type to the screen to check it's a dictionary
# print(type(student_1))
# # 5.Print the value for the key-value pair having the key "stream"
# print(student_1['stream'])
# 6.Print the value for 'completed_lesson_names' - check you can see the list of 3 items
# print(student_1['completed_lessons_names'])
# 7.Print the data type for the value for 'completed_lesson_names' - check it is a list
# print(type(student_1['completed_lessons_names']))
# 8.Print the first element/item in the list of 'completed_lesson_names' (should output "variables")
# firstlesson = student_1['completed_lessons_names'][0]
# print(f"The first lesson is {firstlesson}")
# 9.Change the value of "completed_lessons" to 3
# (an integer not string). Make sure you change was
# successful by printing your dictionary to the screen again.
# student_1['completed_lessons'] = int(3)
# print(student_1)
# 10.	Delete "data_types" from
# the list under the key 'completed_lesson_names'
# student_1['completed_lessons_names'].remove('data types')
# del student_1['completed_lessons'][1:3] ASK TMR
# print(student_1)
# 11.	Use the keys() method on your dictionary to list all the keys
# print(student_1.keys())

# [Task 6]
# Consolidation Task: Practice lists - Waiter Helper
# Starting code:

# Outcome (By doing this you should): Practice using lists and dictionaries
# Script should act like a waiter at a restaurant taking orders

# level 1

# Greet the user

# Print a list of starters

# Take an input for the user for their starter

# Print a list of mains

# Take an input for the user for their main course

# Print a list of desserts

# Take an input for the user for their dessert

# Print all of the user's choices

# level 2
# Use at least one f-string
# Add each item ordered to a list called 'customer_order_list'

# level 3 (may need research if we have not covered dictionaries yet)
# Use dictionaries and assign prices to the items. Create a bill at the end of the program.

# level 4
# Add more to this program. Recommended ways are: Only allow input that is within the list, Add quantities of order etc.

# starter = "bread", "hommas", "carrots", "garllic sauce"
# print('Hi there, I will be your waiter today, this is the starters for today')
# for starter in starter:
#     print(starter)
#
# customerwantstarter = input("Who do you want?")
#
# mains = "fish", "chips", "chicken", "beef"
# print('okay perfect, and for your mains?')
# for mains in mains:
#     print(mains)
#
# customerwantmain = input("So for the mains you'll be having?")
#
# desert = "ice cream", "chocolate", "jelly", "brownie"
# print('okay perfect, and lastly for your desert?')
# for desert in desert:
#     print(desert)
#
# customerwantdesert = input("So for the deserts you'll be having?")
#
# print(f'okay so just to confirm {customerwantdesert}, {customerwantmain} and {customerwantstarter}')

# [Task 7]
# Consolidation Task: Practice dictionaries - Hero Story
# Timings
# 15-30 minutes
# Outcome
# •	Practice using dictionaries to create a Hero Story script
#
# The task
# First part
# •	Define a dictionary called story1
# o	It should have the following keys: 'start', 'middle' and 'end'
# o	The value of each key should relate to the beginning, middle and end of your story
# •	Print the entire dictionary
# •	Print the type of your dictionary
# •	Print only the keys
# •	Print only the values
# •	Print the individual values using the keys
# •	Now, let's add a new key:value pair:
# o	'character':
# •	At the end of the story, print something like: "The end. I hope you enjoyed the story about <print main character using 'character' key>!"

# story1 = {
#     'start': 'There was once a hero...',
#     'middle': 'He saved a cat from a tree...',
#     'end': 'The cat survived...the end. I hope you enjoyed the story',
# }
#
#
# print(type(story1))
#
# print(story1.values())
#
# print(story1.keys())
#
# story1['character']= ''
# print(story1)

# [Task 8]
# (If time) Task: Working with sets
# 🎯 Outcome (By doing this you should): Practice creating sets, adding and removing elements, and learn the properties of sets.
# The task
# 1.	Explain 2 main ways that sets are different to lists and tuples
# 2.	Create a set named 'fruits' containing "apple", "banana", and "cherry".
# 3.	Print the set 'fruits'
# 4.	Add "orange" to the fruits set using one of the set's methods.
# 5.	Print the set 'fruits' - check it's added
# 6.	Remove "banana" from the fruits set using one of the set's methods.
# 7.	Print the set 'fruits' - check it's removed
# 8.	Attempt to add another "apple" to the fruits set. What do you observe? Why does this happen?
# 9.	Print the final fruits set.
# 10.	Print the 2nd item in the set. If there is any problem doing this, explain.

# fruits = {"apple", "banana", "cherry"}
# print(fruits)
#
# fruits.add("orange")
# print(fruits)
#
# fruits.remove("banana")
# print(fruits)
#
# fruits.add("apple")
# print(fruits)

# They can only store new elements, hence apple can only come one time


# print(fruits[1]) NOT WORKING

# tupleconvert= tuple(fruits)
# print(tupleconvert[1])

# [Task 9]
# (If time) Task: Working with frozen sets
# 🎯 Outcome (By doing this you should): Learn the concept and usage of immutable sets (frozen sets).
# The task
# 1.	Create a frozen set named frozen_set containing elements "hello", "world".
# 2.	Try to add "!" to frozen_set. What happens?
# 3.	Create a normal set named normal_set containing elements "let's", "learn".
# 4.	Try to add frozen_set to normal_set. Why does it work? Explain.
# 5.	Print normal_set.
# 6.	Run your script half a dozen times. What do you notice about where frozen_set is added to normal_set? Hint: Look at the order of the items.
# 7.	What makes a frozen set different to a normal set? Explain.

# frozen_set = frozenset({'hello', 'world'})
# # print(frozen_set)
#
# # frozen_set.add ('!')
# # frozen_set.add (')')
# print(frozen_set)
# # does not recognise symbols
#
# ##normal_set = normalset({"'let's'", 'world'}) NOT WORKING ASK
# normal_set = set({"let's", "world"})
# print(normal_set)



