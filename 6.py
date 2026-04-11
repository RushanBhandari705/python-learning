word = input("Enter a word: ")
vowels = "aeiouAEIOUBC"
count = 0

for letter in word:
    if letter in vowels:
        count += 1

print("Number of vowels:", count)
