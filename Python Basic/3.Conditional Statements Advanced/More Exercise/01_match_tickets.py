budget = float(input())
category = input()
people_in_group = int(input())

price = 0
transport = 0

if category == "VIP":
    price = 499.99 * people_in_group
    if 1 <= people_in_group <= 4:
        transport = budget - budget * 0.75
    elif 5 <= people_in_group <= 9:
        transport = budget - budget * 0.60
    elif 10 <= people_in_group <= 24:
        transport = budget - budget * 0.50
    elif 25 <= people_in_group <= 49:
        transport = budget - budget * 0.40
    elif people_in_group >= 50:
        transport = budget - budget * 0.25
elif category == "Normal":
    price = 249.99 * people_in_group
    if 1 <= people_in_group <= 4:
        transport = budget - budget * 0.75
    elif 5 <= people_in_group <= 9:
        transport = budget - budget * 0.60
    elif 10 <= people_in_group <= 24:
        transport = budget - budget * 0.50
    elif 25 <= people_in_group <= 49:
        transport = budget - budget * 0.40
    elif people_in_group >= 50:
        transport = budget - budget * 0.25

diff = abs(transport - price)
if transport > price:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
