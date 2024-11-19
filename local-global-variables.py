'''
message1 = "Global Variable"

def myFunction():
    print("\nINSIDE THE FUNCTION")
    # Global variables are accessible inside a function
    print(message1)
    # Declaring a local variable
    message2 = "Local Variable"
    print(message2)


Calling the function
Remember: myFunction() has no parameters.
So when I call the function,
I have to use a pair of emppty parenthesis.


myFunction()

print("\nOUTSIDE THE FUNCTION")

# Global variables are accessible outside the function and anywhere in the program
print(message1)

# Local variables are only accessible within the function that they're defined
print(message2)
'''

message3 = "Global Variable (shares the same name as a local variable)"

def myFunction2():
    message3 = "Local Variable (shares same name as a global variable)"
    print("\nINSIDE THE FUNCTION")
    print(message3)

# calling the function
myFunction2()

# Printing message3 OUTSIDE the function
print("\nOUTSIDE THE FUNCTION")
print(message3)
