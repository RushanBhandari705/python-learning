#Automatically skip any product with a negative price.
#Add ip all the valid(positive) prices to get a subtotal
#Calculate a 13% tax on the subtotal and include it in the total amount
#Finally, it will ask if the user wants the products delivered. If the answer is yes, an extra delivery fee of 100 will be added to the total.

subtotal = 0

while True:
    product = input("Enter the product name: ")
    price = float(input("Enter the price of the product: "))

    if price < 0:
        print("Invalid price. Product skipped.")
    else:
        subtotal += price

    choice = input("Do you want to add another product? (Yes/No): ").lower()
    if choice == "no":
        break

tax = subtotal * 0.13
total = subtotal + tax

# Delivery option
delivery = input("Do you want the products delivered? (Yes/No): ").lower()
if delivery == "yes":
    total += 100
    
print(f"Subtotal: {subtotal:.2f}")
print(f"Tax (13%): {tax:.2f}")
print(f"Total amount: {total:.2f}")