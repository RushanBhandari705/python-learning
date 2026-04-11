import random

choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)

player = input("Enter rock, paper, or scissor: ")

if player == computer:
    print("It's a tie!")
elif (player == "rock" and computer == "scissors") or \
     (player == "paper" and computer == "rock") or \
     (player == "scissors" and computer == "paper"):
    print("You win!")
else:
    print("You lose! Computer chose", computer)
