#This is a program that will ask for my name and the time. And if the time is after 10am, it will say I should "Get coding ASAP!


#print introduction and ask for user's name
print('Hello! Nice to see you\'re doing some coding practice for your grad scheme app. Pray tell me... what is your name?')
myName = input()
print('Nice to meet you, ', myName, '. And what an absolute legend you are! Well done for coding this silly little program. Keep it up!')


#declare morning and afternoon string variables to search for in user's input
morning = 'am'
afternoon = 'pm'


#prompt user for the time and declare input variable for user time. Then use try-except error handling for the input response.
try:
    userTime = input('By the way, do you happen to have the time on you?\n') #use "\n" to force input onto new line in the console.

    #check if the time contains 'pm' or else assume 'am or catch error.
    #if the time is in the afternoon, then print a panicked message, otherwise print a message about loving morning coding sessions.
    if afternoon in userTime:
        print('Jesus H Christ! Is that the time already? You better get coding boy!')
    elif morning in userTime:
        print('Ah I do love a morning coding session. Godspeed sir!')
    else:
        raise ValueError('Your input did not contain time formatting')
except ValueError as e:
        print(f'The input you typed is not a valid time format: {e}')
