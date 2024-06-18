budget = float(input())
statists = int(input())
price_cloths_per_statist = float(input())

decoration = budget * 10/100

if statists >= 150:
    price_cloths_per_statist *= 90/100

total_cloth_money = statists * price_cloths_per_statist
total_movie_money = decoration + total_cloth_money
money_left = abs(budget - total_movie_money)

if total_movie_money > budget:
    print("Not enough money!")
    print(f"Wingard needs {money_left:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")
