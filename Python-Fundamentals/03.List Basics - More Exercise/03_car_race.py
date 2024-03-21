left_car_time = 0
right_car_time = 0
seq_num = list(map(int, input().split(" ")))
middle_of_list = (len(seq_num) // 2) + 1

for current_time_left in seq_num[0:middle_of_list - 1]:
    if current_time_left != 0:
        left_car_time += current_time_left
    else:
        left_car_time *= 0.8

for current_time_right in seq_num[-1:-middle_of_list:-1]:
    if current_time_right != 0:
        right_car_time += current_time_right
    else:
        right_car_time *= 0.8

if left_car_time < right_car_time:
    print(f"The winner is left with total time: {left_car_time:.1f}")

if left_car_time > right_car_time:
    print(f"The winner is right with total time: {right_car_time:.1f}")