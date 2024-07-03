days = int(input())
type_place = input()
value = input()

price = 0
result = 0
final_price = 0
days = days - 1

if type_place == 'room for one person':
    price = 18.00 * days
    if days <= 10:
        result = 18.00 * days
    elif 10 < days <= 15:
        result = 18.00 * days
    elif days > 15:
        result = 18.00 * days
elif type_place == 'apartment':
    price = 25.00 * days
    if days <= 10:
        result = price - price * 0.30
    elif 10 < days <= 15:
        result = price - price * 0.35
    elif days > 15:
        result = price - price * 0.50
elif type_place == 'president apartment':
    price = 35.00 * days
    if days <= 10:
        result = price - price * 0.10
    elif 10 < days <= 15:
        result = price - price * 0.15
    elif days > 15:
        result = price - price * 0.20

if value == 'positive':
    final_price = result + result * 0.25
elif value == 'negative':
    final_price = result - result * 0.10

print(f"{final_price:.2f}")
