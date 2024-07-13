count_p1, count_p2, count_p3, count_p4, count_p5 = 0, 0, 0, 0, 0
n = int(input())

for index in range(n):
    current_number = int(input())

    if current_number < 200:
        count_p1 += 1
    elif 200 <= current_number <= 399:
        count_p2 += 1
    elif 400 <= current_number <= 599:
        count_p3 += 1
    elif 600 <= current_number <= 799:
        count_p4 += 1
    else:
        count_p5 += 1

p1_percentage = count_p1 * 100 / n
p2_percentage = count_p2 * 100 / n
p3_percentage = count_p3 * 100 / n
p4_percentage = count_p4 * 100 / n
p5_percentage = count_p5 * 100 / n

print(f"{p1_percentage:.2f}%")
print(f"{p2_percentage:.2f}%")
print(f"{p3_percentage:.2f}%")
print(f"{p4_percentage:.2f}%")
print(f"{p5_percentage:.2f}%")
