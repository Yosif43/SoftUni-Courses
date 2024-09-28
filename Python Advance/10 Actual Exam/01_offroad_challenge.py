from collections import deque

fuel_seq = deque([int(el) for el in input().split()])
consumption_seq = deque([int(el) for el in input().split()])
needed_fuel_seq = deque([int(el) for el in input().split()])

reached_altitudes = []

for i in range(4):
    last_fuel = fuel_seq.pop()
    first_consumption = consumption_seq.popleft()
    required_fuel = needed_fuel_seq.popleft()

    remaining_fuel = last_fuel - first_consumption

    if remaining_fuel >= required_fuel:
        print(f"John has reached: Altitude {i + 1}")
        reached_altitudes.append(i + 1)
    else:
        print(f"John did not reach: Altitude {i + 1}")
        break

if len(reached_altitudes) == 4:
    print("John has reached all the altitudes and managed to reach the top!")
elif reached_altitudes:
    print("John failed to reach the top.")
    print("Reached altitudes: " + ", ".join(f"Altitude {x}" for x in reached_altitudes))
else:
    print("John failed to reach the top.")
    print("John didn't reach any altitude.")
