import math

num = float(input("Enter a number: "))

if num >= 0:
    result = math.sqrt(num)
    print("Square root =", result)
else:
    print("Square root is not defined for negative numbers.")