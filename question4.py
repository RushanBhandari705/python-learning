#Write a program that creates and prints out a list containing only the unique elements from an existing list.
#[1,1,2,3,3,4,4,5,6,5,6] -> [1,2,3,4,5,6]

input_list = [1, 1, 2, 3, 3, 4, 4, 5, 6, 5, 6]
unique_list = []
for item in input_list:
    if item not in unique_list:
        unique_list.append(item)
print(unique_list)