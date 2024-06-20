from math import ceil

show_name = str(input())
episode_time = int(input())
brake_time = int(input())

lunch_break = brake_time * 1/8
fresh_air_time = brake_time * 1/4
time_left = brake_time - lunch_break - fresh_air_time
free_time = ceil(abs(time_left - episode_time))


if time_left >= episode_time:
    print(f"You have enough time to watch {show_name} and left with {free_time} minutes free time.")
else:
    print(f"You don't have enough time to watch {show_name}, you need {free_time} more minutes.")
