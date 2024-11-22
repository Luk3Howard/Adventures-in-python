'''
CHATGPT PRACTICE QUESTION SET

#BASIC VARIABLES AND DATA TYPES
'''
# 1 - Assigning Variables
# Create a variable named "school" and assign it the value "Edinburgh University"
school = "Edinburgh University"
print(school)
# What data type is the variable school?
# A: string

### Numeric Operations:

# Create two variables, x set to 10 and y set to 3.
x,y = 10, 3
print(x, y)

# Calculate and print the result of x divided by y.
print(x/y)

# Calculate the remainder of x divided by y.
print(x%y)

### Strings:

# Create a string variable named greeting that contains "Hello, world!".
greeting = "Hello, world!"
print(greeting)

# Print the length of greeting.
print(len(greeting))

# Use slicing to print only "world" from greeting.
extracted = greeting[7:12]
print(extracted)

###Lists:

# Create a list named numbers containing the following numbers: 1, 2, 3, 4, and 5.
numbers = [1, 2, 3, 4, 5]
print(numbers)

# Append the number 6 to numbers and print the updated list.
numbers.append(int(6))
print(numbers)

# Print the third item in the numbers list.
print(numbers[2])

### Control Structures
## Conditionals:

# Write a Python script that checks if a variable a is greater than 10. If it is, print "Greater than 10." Otherwise, print "10 or less."
a = 7
if a > 10:
    print("Greater than 10")
else:
    print("10 or less")

## Loops:

# Using a for loop, iterate over the list [1, 2, 3, 4, 5] and print each number squared.
#for (numbers):
 #   print(i**2)

## Combining Conditionals and Loops:

# Write a for loop that prints all even numbers from 1 to 20.


# Modify the loop to exclude the number 10.

### Functions

##Basic Function:
'''
Define a function square that takes one argument and returns the square of that argument.
Call the function with the value 4 and print the result.
Function with Conditionals:

Write a function max_number that takes three arguments and returns the largest of the three. Do not use the built-in max() function.
Using Functions with Lists:

Define a function sum_list that takes a list of numbers as an argument and returns the sum of those numbers.
Test the function with the list [1, 2, 3, 4, 5].
'''