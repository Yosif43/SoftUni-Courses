flower_type = input()
count_flowers = int(input())
budget = int(input())

total_sum = 0
if flower_type == 'Roses':
    total_sum = count_flowers * 5
    if count_flowers > 80:
        total_sum = total_sum - total_sum * 0.10
elif flower_type == 'Dahlias':
    total_sum = count_flowers * 3.80
    if count_flowers > 90:
        total_sum = total_sum - total_sum * 0.15
elif flower_type == 'Tulips':
    total_sum = count_flowers * 2.80
    if count_flowers > 80:
        total_sum = total_sum - total_sum * 0.15
elif flower_type == 'Narcissus':
    total_sum = count_flowers * 3
    if count_flowers < 120:
        total_sum = total_sum + total_sum * 0.15
elif flower_type == 'Gladiolus':
    total_sum = count_flowers * 2.50
    if count_flowers < 80:
        total_sum = total_sum + total_sum * 0.20

diff = abs(total_sum - budget)
if total_sum <= budget:
    print(f"Hey, you have a great garden with {count_flowers} {flower_type} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")
