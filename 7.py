print("Welcome to Python")

balance = 1000
correct_pin = "1234"

pin = input("Enter your PIN: ")

if pin == correct_pin:

    while True:
        print("\n----- ATM Menu -----")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print("Your balance is:", balance)

        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                balance += amount
                print("Money deposited successfully.")
            else:
                print("Invalid amount.")

        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            if amount > balance:
                print("Insufficient balance.")
            elif amount <= 0:
                print("Invalid amount.")
            else:
                balance -= amount
                print("Please collect your cash.")

        elif choice == "4":
            print("Thank you for using ATM.")
            break

        else:
            print("Invalid option. Try again.")

else:
    print("Wrong PIN. Access Denied.")
