count_groups = int(input())

total_people = 0
count_groups_5 = 0
count_groups_6_12 = 0
count_groups_13_25 = 0
count_groups_26_40 = 0
count_groups_41 = 0

for i in range(count_groups):
    count_people = int(input())
    total_people = total_people + count_people
    if count_people <= 5:
        count_groups_5 += count_people
    elif 6 <= count_people <= 12:
        count_groups_6_12 += count_people
    elif 13 <= count_people <= 25:
        count_groups_13_25 += count_people
    elif 26 <= count_people <= 40:
        count_groups_26_40 += count_people
    elif count_people >= 41:
        count_groups_41 += count_people

print(f"{count_groups_5 / total_people * 100:.2f}%")
print(f"{count_groups_6_12 / total_people * 100:.2f}%")
print(f"{count_groups_13_25 / total_people * 100:.2f}%")
print(f"{count_groups_26_40 / total_people * 100:.2f}%")
print(f"{count_groups_41 / total_people * 100:.2f}%")
