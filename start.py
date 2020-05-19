#Name: Jillian Johnson
#Team: Data Analychicks
#Members: Lily Anne H., Claudia A., Morgan H.
#Welcome to the Data Analychicks Guess the Number Game!!! This program is a game where users can take a shot at guessing
#what number the master computer is thinking.
#Resources: https://inventwithpython.com/invent4thed/
#           https://www.w3schools.com/python/default.asp
#           https://stackoverflow.com/questions/39743789/how-do-you-make-a-leaderboard-in-python

# 05/08/2020-Write python Pseudo Code/plan out game
# 05/12/2020-Replace pseudo code with python for part one: Intro Only
# 05/14/2020-Replace pseudo code with python for part two: Game Loop
# 05/15/2020-EXTRA create LeaderBoard


#import proper modules
import random
import pygame
#Necessary Functions

def text(txtArr):#This function takes an array of text and returns it as a paragraph
    delim = " "
    print(delim.join(txtArr))

#PROGRAM INTRO PSEUDO CODE
# 05/12/2020-Replace pseudo code with python for part one: Intro Only
def intro():
    #Welcome user to game
    user_name = input("Enter your username: ") #Prompt user to input their name
    #prompt user [by name] if they need directions on how to play the game
    greeting = ["Hello", user_name, ".", "Do you need instructions on how to play Guess The Number(Y/N)?"]
    text(greeting)
    user_repsonse = input().upper() #Get & Store user response
    returnVal = [user_repsonse, user_name] #Place stored values in an array
    return returnVal #Return array of stored values to be accessed by index.

def da_Rules (returnVal):
    if str(returnVal[0]) == 'Y':#if user response equal to 'Yes' display directions
        repeat = 'Y'
        while repeat == 'Y':
            rules = [
                '''The computer will think of a secret number from 1 to 20 and ask you to guess it.
                After each guess, the computer will tell you whether the number is too high or too low. 
                If you can guess the number within 6 tries, you win.''',
                'Would you like me to repeat the rules again', returnVal[1], "(Y/N) ?"]
            text((rules))
            repeat = input().upper()
            if str(repeat) == 'N':
                game_Loop(returnVal)
    elif str(returnVal[0]) == 'N':
        print("Continuing to game loop")
        game_Loop(returnVal)
    else:
        print("INVALID RESPONSE. RETURNING TO MAIN MENU")
        da_Rules(intro())

# Session 1 Reflection: Claudia and Lily are heavily engaged with the project and express an eagerness to learn. Lily has
# made a consistent effort to be lead programmer. I covered different variables and data types, the difference between
# creating and calling functions, accessing items within a list, and passing values to a function. Next session I would
# like to cover these same topics and allow for us to practice them more. Must also introduce imports and program flow.

# 05/14/2020-Replace pseudo code with python for part two: Game Loop
# 05/17/20 We wound up finishing the game loop today. Learned the importance of placing game vars within for loop so
# they "refresh" with each game played.
# 
def game_Loop(nameAccess):

    flag = 'Y'
    while flag == 'Y':# While flag variable is equal to true
        #Key game vars must go inside while loop so that they change upon re-playing the game
        guess_Count = 0  # create variable for storing user guesses and set to 0
        key_Num = random.randint(1, 20)  # create variable for storing random number and set to a random number
        for guesses in range(6):
            getGuessStr = ["I'm thinking of a whole number between 1 and 20. Can you guess what it is", nameAccess[1], "?" ]
            text(getGuessStr)
            user_guess = input()
            user_guess = int(user_guess)
            guess_Count+= 1

            if user_guess > key_Num:
                print("Your guess is too high.")
            if user_guess < key_Num:
                print("Your guess is too low")
            if user_guess == key_Num:
                break

        if user_guess == key_Num:
            # congratulate user and ask if they would like to play_again
            print("Good work " + nameAccess[1] +" you did it! And after only " + str(guess_Count) +" guesses!")
            flag = input("Would you like to play again (Y/N)?").upper()
        elif user_guess != key_Num:
            print("Sorry. You lose. The number I was thinking of was " + str(key_Num))
            flag = input("Would you like to play again (Y/N)?").upper()

    print("Thanks for playing!")

#PROGRAM BEGINS HERE####################################################################################################
### FUNCTION CALLS ############################### FUNCTION CALLS ############################ FUNCTION CALLS ##########
da_Rules(intro())






