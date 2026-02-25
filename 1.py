#Write a program that asks the user to enter two number A and B and then code to swap your values of A and B and print them out.
A= int(input("Enter the first number:"))
B=int(input("Enter the second number:"))
print("Your first number is:", A, "and Your second number is:", B)
temp=A
A=B
B=temp
print("The numbers after swap is:", A,B)