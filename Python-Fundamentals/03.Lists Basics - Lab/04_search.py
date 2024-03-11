n = int(input())
special_word = input()
special_list = []
filtered_list = []

for lines in range(n):
    user_input = input()
    special_list.append(user_input)

print(special_list)

filtered_list = special_list
for filter_element in range(len(special_list) - 1, -1, -1):
    if special_word not in filtered_list[filter_element]:
        filtered_list.remove(filtered_list[filter_element])

print(filtered_list)