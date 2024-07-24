input_line = input()
sum_steps = 0
goal = 10000

while input_line != 'Going home':
    steps = int(input_line)
    sum_steps += steps

    if sum_steps >= goal:
        break

    input_line = input()

if input_line == 'Going home':
    steps_home = int(input())
    sum_steps += steps_home

diff = abs(goal - sum_steps)
if sum_steps >= goal:
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")