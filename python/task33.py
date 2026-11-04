import random
num1 = random.randint(1,100)
num2 = random.randint(1,100)
num3 = random.randint(1,100)
num4 = random.randint(1,100)
num5 = random.randint(1,100)
score = 0
num1_guess = int(input("Round One! Guess a number from 1 to 100: "))
if num1_guess > num1:
    print