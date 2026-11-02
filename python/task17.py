minutes = int(input("Enter any number of minutes: "))
hours = minutes // 60
minutes_left = minutes % 60
print(str(minutes) + " minutes is " + str(hours) + " hour(s) and " + str(minutes_left) + " minute(s)")
