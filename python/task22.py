age = int(input("Enter your age: "))
if age >= 17:
    print("You are old enough to drive")
else:
    years_left = 17 - age
    print("You can drive in " + str(years_left) + " years")