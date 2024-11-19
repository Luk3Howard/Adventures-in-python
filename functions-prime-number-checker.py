#Determine if a given number by the user is a prime number.


def checkIfPrime (numberToCheck):
    if numberToCheck <=1:
        return False # Numbers less than or equal to 1 can't be prime
    for i in range(2, int(numberToCheck**0.5)+1): #only check up to the square root
        if (numberToCheck % i) == 0:
            return  False
    return True # If no factors were found, then the number must be prime.


# Create the main loop to continue asking for a number until a prime one is found
while True:
    print('Enter a number to check if it\'s prime: ')
    try:
        numberToCheck = int(input()) #convert user input string to integer
        if checkIfPrime(numberToCheck):
            print(f"{numberToCheck} is a prime number.")
            break # break the loop if the number is prime
        else:
            print(f"{numberToCheck} is not a prime number. Please try again.")
    except ValueError: # adding error validation for inputs that are not integers
        print("Invalid input! Please enter a valid whole number.")
