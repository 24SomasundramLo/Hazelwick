temp = float(input("What is the temperature in Celsius: "))
if temp < 0:
    print("It is freezing")
elif 0 <= temp <= 20:
    print("Wow, cold weather")
elif 21 <= temp <= 30:
    print("Nice, warm")
else:
    print("Very hot")