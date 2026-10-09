import random
num = random.randint(1, 6)
word = ""
match num:
    case 1:
        word = "one"
    case 2:
        word = "two"
    case 3:
        word = "three"
    case 4:
        word = "four"
    case 5:
        word = "five"
    case 6:
        word = "six"
    case _:
        word = "... how did you get this?"
print("The number I generated is " + word)