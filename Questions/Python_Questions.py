
# # 1. Write a Python program to check if a number is positive, negative, or zero using if-elif-else.

# number = float(input("enter a number :- "))

# if number < 0:
#      print("Negavite Number")
# elif number > 0:
#     print("Positive Number")
# else:
#     print("Number is zero")


# # 2. Create a program to find the largest of three numbers using conditional statements.

# num1 = float(input("Enter first Number :- "))
# num2 = float(input("Enter second Number :- "))
# num3 = float(input("Enter third Number :- "))

# if num1 >= num2 and num1 >=num3:
#     print(f"greatest Number is {num1}")
# elif num2 >= num1 and num2 >=num3:
#     print(f"greatest Number is {num2}")
# else:
#     print(f"greatest Number is {num3}")

# # 3. Write a program to print the first 10 natural numbers using a for loop.

# print("First 10 Natural Numbers Are :- ")

# for num in range(1,11):
#     print(num)

# num = 1 

# for num in range(10):
#     print(num + 1)

# while num <= 10:
#     print(num)
#     num +=1


# 4. Write a Python program to generate a list of squares of numbers from 1 to 10 using a list comprehension.

square = [num**2 for num in range(1,11)]

print("list of squares of numbers from 1 to 10 Using list comprehension: :- " , square)

# ***** Using For Loop

listSquare = []

for num in range(1,11):
    listSquare.append(num**2)

print("list of squares of numbers from 1 to 10 using for Loop :- " , listSquare)

# ______________________________________________________________

# 5. Write a Python program to demonstrate the use of break, continue, and pass statements in loops.

print("Demonstrating break:")
for i in range(1,11):
    if i == 5:
        break
    print(i)

print("\nDemonstrating continue :")
for i in range(1,11):
    if i == 5:
        continue
    print(i)

print("\nDemonstrating pass :")
for i in range(1,11):
    if i == 5:
        pass
    print(i)

""" 
Explanation => 

Break: The loop stops completely when the condition i == 5 is met.

Continue: The loop skips the current iteration when i == 5 and proceeds to the next iteration.

Pass: The pass statement does nothing—it serves as a placeholder and allows the loop to continue normally.

"""