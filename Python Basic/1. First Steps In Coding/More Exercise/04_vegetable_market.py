price_kg_veg = float(input())
price_kg_fruit = float(input())
total_kg_veg = int(input())
total_kg_fruit = int(input())

euro = 1.94
vegetables = total_kg_veg * price_kg_veg
fruit = total_kg_fruit * price_kg_fruit
total = (vegetables + fruit) / euro

print(f"{total:.2f}")