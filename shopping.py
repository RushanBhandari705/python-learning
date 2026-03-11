#This program helps users keep track of their shopping total. It will:
#Ask the user to enter the name and price of a product. Continue asking for more products until the user says "No" when asked 
#if they want to add another one

total = 0

while True:
    product = input("Enter the product name: ")
    price = float(input("Enter the price of the product:"))

    total += price

    choice = input("Do you want to add another product? (Yes/No): ").lower()

    if choice == "no":
        break

print(f"\nTotal cost of your shopping:{total:.2f}")

