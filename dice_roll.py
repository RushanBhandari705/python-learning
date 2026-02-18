import random

print("Welcome to Dice Rolling Game")

while True:
    input("Press Enter to roll the dice")
    dice = random.randint(1, 6)
    print("You rolled a", dice)

    again = input("Do you want to roll again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing")
        break
