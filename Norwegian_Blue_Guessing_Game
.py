# Brogan Mutarelli
# 10/18/17
# Norwegian Blue Guessing Game
# A Guessing Game

import random

#display title and intructions
print("*" * 80)
print("THE NORWEGIAN BLUE GUESSING GAME")
print("*" * 80)

istructions = """You walk into a pet store and need to guess thae age of the Nerwegian Blue Parrot.
 The pet shop owner greets you and says you need to guess the age of the parrot in five guesses.
 If you do you can take it home."""


print(istructions)

#Make up the parrot age
parrot_age=random.randint(1, 20)

#set the number of guesses to 0
number_of_guess=0

while number_of_guess < 5:
    #Get a number from the user
    guess=input("Guess the age of the parrot [1 to 20]")
    guess=int(guess) #Converts guess into an interger and stores it in guess
    number_of_guess = number_of_guess + 1
    print(" " * 80)
    if guess == parrot_age:
        print("You Win")
        break
    else:
        print("That was a horrible guess!!!!")
        print(" " * 80)
        if guess > parrot_age:
            print(" " * 80)
            print("Too High")
            print(" " * 80)
        else:
            print(" " * 80)
            print ("Too Low")
            print(" " * 80)

print ("Thank You For Playing. The parrot was" , parrot_age, "years old.")



