while True:
    price = 0
    hours = float(input("How many hours have you parked for: "))
    if hours == 0:
        break
    car_type = input("Is your car electric: ")
    if car_type.lower() == "yes":
        price = 2 * hours
        print("Your parking fee is £" + str(price) + "0")
    else:
        price = 4 * hours
        print("Your parking fee is £" + str(price) + "0")