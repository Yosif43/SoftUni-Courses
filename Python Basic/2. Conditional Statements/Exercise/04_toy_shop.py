travel_price = float(input())
a_puzzles = int(input())
a_dolls = int(input())
a_bears = int(input())
a_minions = int(input())
a_truck_toys = int(input())

puzzle = 2.60
doll = 3
bear = 4.10
minion = 8.20
truck = 2

sell_money = (a_puzzles * puzzle) + (a_dolls * doll) + \
             (a_bears * bear) + (a_minions * minion) + (a_truck_toys * truck)
amount_toys = a_truck_toys + a_bears + a_minions + a_dolls + a_puzzles

if amount_toys >= 50:
    sell_money *= 75/100

sell_money *= 90/100

if sell_money >= travel_price:
    print(f"Yes! {sell_money - travel_price:.2f} lv left.")
else:
    print(f"Not enough money! {travel_price - sell_money:.2f} lv needed.")