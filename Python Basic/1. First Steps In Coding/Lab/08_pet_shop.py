dog_food_qty = int(input())
cat_food_qty = int(input())

cat_total_price = cat_food_qty * 4
dog_total_price = dog_food_qty * 2.5
total_price = cat_total_price + dog_total_price

print(f"{total_price} lv.")