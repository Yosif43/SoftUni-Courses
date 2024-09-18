from collections import deque

daily_food_supplies = list(map(int, input().split(", ")))
daily_stamina = deque(int(el) for el in input().split(", "))
mountains_conquered = []
day = 1
mountains = deque([("Vihren", 80),
             ("Kutelo", 90),
             ("Banski Suhodol", 100),
             ("Polezhan", 60),
             ("Kamenitza", 70)
])

while True:
    if len(mountains_conquered) == 5:
        print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
        break
    if day > 7 or not daily_food_supplies or not daily_stamina:
        print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
        break
    last_daily_food = daily_food_supplies.pop()
    first_daily_stamina = daily_stamina.popleft()
    total_sum = last_daily_food + first_daily_stamina
    next_mountain = mountains.popleft()
    if total_sum >= next_mountain[1]:
        mountains_conquered.append(next_mountain[0])
        day += 1
    else:
        mountains.appendleft(next_mountain)
        day += 1


if mountains_conquered:
    print("Conquered peaks:")
    for peak in mountains_conquered:
        print(peak)



