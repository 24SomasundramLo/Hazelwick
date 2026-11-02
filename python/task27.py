test_score = int(input("Enter a score from a test out of 100: "))
if 100 >= test_score >= 90:
    print("You get an A!")
elif 80 <= test_score <=89:
    print("You get a B!")
elif 70 <= test_score <=79:
    print("You get a C!")
elif 60 <= test_score <=69:
    print("You get a D!")
elif 0 <= test_score <= 60:
    print("You failed")
else:
    print("Either you entered a negative score, or went over 100. Either way put a different answer in")