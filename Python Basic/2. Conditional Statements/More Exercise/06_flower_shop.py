from math import floor
from math import ceil


amount_magnolia = int(input())
amount_hyacinth = int(input())
amount_roses = int(input())
amount_cactus = int(input())
gift_price = float(input())

magnolia = 3.25
hyacinth = 4
roses = 3.5
cactus = 8

total_magnolia = amount_magnolia * magnolia
total_hyacinth = amount_hyacinth * hyacinth
total_roses = amount_roses * roses
total_cactus = amount_cactus * cactus
total_sum = (total_magnolia + total_hyacinth + total_roses + total_cactus)
total_sum = abs((0.05 * total_sum) - total_sum)
total_money = (gift_price - total_sum)

if total_money > 0:
    print(f"She will have to borrow {ceil(abs(total_money))} leva.")
else:
    print(f"She is left with {floor(abs(total_money))} leva.")

