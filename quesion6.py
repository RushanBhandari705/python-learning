#Write a python program that:
#In the given list:
#[1,2,6,4,5,7,6,7,8,1,4,5]
#Counts how many times each number appears
#Displays only the number that are repeated(appear more than once) and how many times they appear.

input_list = [1, 2, 6, 4, 5, 7, 6, 7, 8, 1, 4, 5]
count_dict = {}
for num in input_list:
    count_dict[num] = count_dict.get(num, 0) + 1
for num, count in count_dict.items():
    if count > 1:
        print(f"{num}: {count}")
        