score = 0

answer = input("What is the capital of France? ")
if answer.lower() == "paris":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("What is 5 * 6? ")
if answer == "30":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("Your final score is :", score)
