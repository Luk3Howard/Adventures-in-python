# This program says hello and asks for my name and age.
# It then finds the length of characters in their name, and calculates how old they'll be in one year


print('Hello World')
print('What is your name?')     # ask for user's name

myName = input()
print('Nice to meet you ' + myName)

print('The length of your name is: ')
print(len(myName))

print('What is your current age?: ')
myAge = input()
print('You will be ' +str(int(myAge) + 1) + ' in a year (or sooner!).')




