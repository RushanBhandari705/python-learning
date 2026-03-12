#write a program that takes N numbers as input from a user and puts them in a list.
#Then the program should find out the sum of all the odd numbers and the sum of all the even numbers form the list

N = int(input("Enter how many numbers you want to input: "))

numbers = []

for i in range(N):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

odd_sum = 0
even_sum = 0

for num in numbers:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

print("List of numbers:", numbers)
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)
