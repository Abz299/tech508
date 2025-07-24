# Mini-calculator
# from maths_operation import* #gives all
# from maths_operation import add #only gives add function
import maths_operation

first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the first number: "))
result = maths_operation.add(first_num, second_num) #another way

print(f"{first_num} + {second_num} = {result}")