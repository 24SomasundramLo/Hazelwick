
import random

num = random.randint(1, 100)
num_guess = 0
attempts = 0

while num_guess != num and attempts < 10:
    num_guess = int(input("Guess a number from one to one hundred: "))
    attempts = attempts + 1

    if num_guess > num:
        print("Too high, guess again.")

    elif num_guess < num:
        print("Too low, guess again.")

    else:
        print("Good job, you got it!")

if num_guess != num:
    print("You lost! You've used all 10 attempts.")
    print("The number was " + str(num))