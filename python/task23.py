score = 0
add_answer = int(input("What is 35 + 16: "))
if add_answer == 51:
    print("Good job!")
    score = score + 1
else:
    print("Ooh sorry, the answer was 51")
    score = score + 0

subtract_answer = int(input("What is 84 - 23: "))
if subtract_answer == 61:
    print("Good job!")
    score = score + 1
else:
    print("Ooh sorry, the answer was 61")
    score = score + 0

multiply_answer = int(input("What is 13 x 6: "))
if multiply_answer == 78:
    print("Good job!")
    score = score + 1
else:
    print("Ooh sorry, the answer was 78")
    score = score + 0

divide_answer = int(input("What is 169 ÷ 13: "))
if divide_answer == 13:
    print("Good job!")
    score = score + 1
else:
    print("Ooh sorry, the answer was 13")
    score = score + 0

print("Your score is " + str(score) + " out of 4")