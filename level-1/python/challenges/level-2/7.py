# 7.​ Create a basic number guessing game.
from random import randint

random_num = randint(1, 10)

user_guess = int(input("Guess a number between 1 and 10: "))

while user_guess != random_num:
    user_guess = int(input("Try again: "))
    random_num = randint(1, 10)


print("You guessed it right!")
