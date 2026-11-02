print("Welcome to OCR Land!")

allowed = 0

while allowed < 8:
    height = float(input("Enter the rider's height in cm: "))

    if height >= 140:
        print("You can ride on your own")
        allowed = allowed + 1

    elif height >= 120:
        adult = input("Are you riding with an adult? (yes/no): ")

        if adult == "yes":
            print("You can ride")
            allowed = allowed + 1
        else:
            print("You cannot ride")

    else:
        print("You cannot ride")

print("8 people have been allowed to ride!")