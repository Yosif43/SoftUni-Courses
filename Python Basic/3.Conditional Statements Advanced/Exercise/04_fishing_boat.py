budget = int(input())
season = input()
count_fishers = int(input())

price = 0
if season == 'Spring':
    price = 3000
elif season == 'Summer' or season == 'Autumn':
    price = 4200
elif season == 'Winter':
    price = 2600

if count_fishers <= 6:
    price *= 0.90
elif 7 <= count_fishers <= 11:
    price *= 0.85
elif count_fishers >= 12:
    price *= 0.75

if count_fishers % 2 == 0:
    if season != 'Autumn':
        price *= 0.95

diff = abs(price - budget)
if price > budget:
    print(f"Not enough money! You need {diff:.2f} leva.")
else:
    print(f"Yes! You have {diff:.2f} leva left.")
