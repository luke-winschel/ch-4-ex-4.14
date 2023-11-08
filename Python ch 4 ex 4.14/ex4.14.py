#Exercise 4.14
#(Computer-Assisted Instruction)  Wrtite a script to help elemtry students learn multiplication.  Create a function that generates two random numbers and gives feedback for each answer

#import the random library
import random

#Define the function that generates the two numbers and gets the user input
def problem ():
    #Establish local variables
    first_rand = random.randrange(0,10)
    second_rand = random.randrange(0,10)
    answer = first_rand * second_rand
    user_answer = -1
    #While statement the propmts user to answer equation and then gives feed back
    while user_answer != answer:
        user_answer =int (input(f'What is {first_rand} * {second_rand}?  '))
        if user_answer == answer:
            print('Correct.  Very Good!')
        else:
            print('No. Try Again')
         
#Define second function that continues looping the problem function
def looping():
    #Runs continuously because there is no value that chages to false
    while True:
        #Calls the problem function over again
        problem()
        
#Run the looping function
looping()