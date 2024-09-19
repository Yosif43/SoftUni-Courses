def reward_duckies(programmer_times, tasks):
    ducks = {
        "Darth Vader Ducky": 0,
        "Thor Ducky": 0,
        "Big Blue Rubber Ducky": 0,
        "Small Yellow Rubber Ducky": 0
    }

    while programmer_times and tasks:
        calculated_time = programmer_times[0] * tasks[-1]

        if 0 <= calculated_time <= 60:
            ducks["Darth Vader Ducky"] += 1
            programmer_times.pop(0)
            tasks.pop()
        elif 61 <= calculated_time <= 120:
            ducks["Thor Ducky"] += 1
            programmer_times.pop(0)
            tasks.pop()
        elif 121 <= calculated_time <= 180:
            ducks["Big Blue Rubber Ducky"] += 1
            programmer_times.pop(0)
            tasks.pop()
        elif 181 <= calculated_time <= 240:
            ducks["Small Yellow Rubber Ducky"] += 1
            programmer_times.pop(0)
            tasks.pop()
        else:
            tasks[-1] -= 2
            programmer_times.append(programmer_times.pop(0))

    print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
    for ducky, count in ducks.items():
        print(f"{ducky}: {count}")

programmer_times = [int(x) for x in input().split()]
tasks = [int(x) for x in input().split()]
reward_duckies(programmer_times, tasks)
