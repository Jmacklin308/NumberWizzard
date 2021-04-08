#######################################################################
# Number guessing game:
# takes in an input from the player and gives them 6 tries at guessing it
#######################################################################


# import random library
import random
import decimal
import os

#Game properties
playerGuesses = 6
guessesTaken = 0
gameOn = True
totalWins = 0
totalLosses = 0 

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

#clear the screen 
clearConsole()

playerName = input("What is your first name?\n")

while gameOn:
    clearConsole()
    #set lucky number
    luckyNumber = random.randint(1,20)
    print(f"Hello there {playerName}! Please pick an number between 1 and 20:")
    print(f"(DEBUG)lucky number is {luckyNumber}")
    for guessesTaken in range(1, playerGuesses+1):
        #ask for first result
        print(f"You have {playerGuesses - guessesTaken} guesses left!")
        playerInput = int(input())
        if playerInput < luckyNumber:
            print("You guessed too low! Please guess again:")
        elif playerInput > luckyNumber:
            print("You guesses too high! Please guess again:")
        else:
            break
        
    if playerInput == luckyNumber:
        print(f"Congrats! You picked my lucky number {luckyNumber}!!!\n")
    else: 
        print(f"Sorry the number I was thinking of is {luckyNumber}!!!\n")
        
    print(f"Would you like to keep playing {playerName}? (Y/N)")
    gameRestart = input()
    x = False
    while x == False:
        if gameRestart == "N":
            print("Thanks for playing! Program closing.")
            gameOn = False #exit program
            break
        elif gameRestart == "Y":
            print("Sweet lets keep playing!!!")
            break
        else:
            print("Please Type Y or N \n ")
            
            
            
