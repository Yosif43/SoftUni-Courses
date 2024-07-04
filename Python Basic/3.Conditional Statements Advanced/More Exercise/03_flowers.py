chryzanthemum = int(input())
roses = int(input())
orchid = int(input())
season = input()
festive = input()

price = 0
total_sum = price + 2
flowers = chryzanthemum + roses + orchid


if season == "Spring":
    price = (chryzanthemum * 2) + (roses * 4.10) + (orchid * 2.50)
    if orchid > 7:
        price = price - price * 0.05
elif season == "Summer":
    price = (chryzanthemum * 2) + (roses * 4.10) + (orchid * 2.50)
elif season == "Autumn":
    price = (chryzanthemum * 3.75) + (roses * 4.50) + (orchid * 4.15)
elif season == "Winter":
    price = (chryzanthemum * 3.75) + (roses * 4.50) + (orchid * 4.15)
    if roses >= 10:
        price = price - price * 0.10
if festive == "Y":
    price = price + price * 0.15

if flowers > 20:
    price = price - price * 0.2

total_sum = price + 2
print(f"{total_sum:.2f}")
