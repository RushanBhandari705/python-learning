#a program that takes two number as input and performs calculations

print("Simple Calculator")
#taking input from the user
num1= float(input("Enter the first number: "))
operator=input("Enter the operator(+,-,*,/): ")
num2=float(input("Enter the second number: "))

#performing calculations
if operator == "+":
    print("Result:", num1 + num2)

elif operator == "-":
    print("Result:", num1-num2)

elif operator == "*":
    print("Result:", num1*num2)

elif operator == "/":
    if num2 !=0:
        print("Result", num1/num2)
    else:
        print("Error!")

else:
    print("Invalid operator!")

