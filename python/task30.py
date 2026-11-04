side_1 = float(input("Enter the length of one side of a triangle: "))
side_2 = float(input("Enter the length of another side of this triangle: "))
side_3 = float(input("Enter the length of the last side of this triangle: "))
if side_1 == side_2 ==  side_3:
    print("Your triangle is equilateral")
elif side_1 == side_2 or side_1 == side_3 or side_2 == side_3:
    print("Your triangle is isosceles")
else:
    print("Your triangle is scalene")