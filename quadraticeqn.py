import math

a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

d = b**2 - 4*a*c   # discriminant

if d >= 0:
    x1 = (-b - math.sqrt(d)) / (2*a)
    x2 = (-b + math.sqrt(d)) / (2*a)

    print("Root using - sign =", x1)
    print("Root using + sign =", x2)
else:
    print("Roots are complex")