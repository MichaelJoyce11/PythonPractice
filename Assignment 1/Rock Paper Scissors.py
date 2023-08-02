#import random.
import random

#define the rock paper scissors funtion. 
def rock_paper_scissors():
    #have 3 choices. 
    options = ["rock", "paper", "scissors"]
    #get users choice.
    user = input("Enter your choice (rock, paper, or scissors): ")
    #generate computer choice at random from the 3 choices. 
    cmp = random.choice(options)

    #display them as if you throw your hands out. 
    print("Your hand:", user)
    print("Computer's hand:", cmp)

    #do an elif for the possibilities of a tie, a win, and a loss for you. 
    if user == cmp:
        print("It's a tie!")
    elif (user == "rock" and cmp == "scissors") or \
         (user == "paper" and cmp == "rock") or \
         (user == "scissors" and cmp == "paper"):
        print("You win! you are better than the computer")
    else:
        print("You lost, the computer won.")

#say lets play (start of chat)
play = input("lets play rock paper scissors? ")

#ask to play again, and if yes, keep going until anything else.
while play == "yes":
    rock_paper_scissors()
    play = input("Keep going? ")
