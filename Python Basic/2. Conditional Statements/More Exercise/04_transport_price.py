km = int(input())
day_night = input()

taxi_day = 0.7 + 0.79 * km
taxi_night = 0.7 + 0.90 * km

bus = 0.09 * km

train = 0.06 * km

if km < 20:
    if day_night == "day":
        print(f"{taxi_day:.2f}")
    else:
        print(f"{taxi_night:.2f}")
if 20 <= km < 100:
    print(f"{bus:.2f}")
if km >= 100:
    print(f"{train:.2f}")