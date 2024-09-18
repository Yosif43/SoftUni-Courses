from collections import deque

caffeine_sequence = deque(map(int, input().split(", ")))
drink_sequence = deque(map(int, input().split(", ")))

stamat_caffeine = 0

while caffeine_sequence and drink_sequence:
    last_caffeine = caffeine_sequence.pop()
    first_drink = drink_sequence[0]
    drink_caffeine = last_caffeine * first_drink

    if stamat_caffeine + drink_caffeine <= 300:
        stamat_caffeine += drink_caffeine
        drink_sequence.popleft()
    else:
        drink_sequence.append(drink_sequence.popleft())
        stamat_caffeine = max(stamat_caffeine - 30, 0)

if drink_sequence:
    print(f"Drinks left: {', '.join(map(str, drink_sequence))}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {stamat_caffeine} mg caffeine.")
