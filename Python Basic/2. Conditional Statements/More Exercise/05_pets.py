from math import ceil
from math import floor

days = int(input())
left_food = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day = float(input())

turtle_food_kg = turtle_food_per_day / 1000
dog_food = dog_food_per_day * days
cat_food = cat_food_per_day * days
turtle_food = turtle_food_kg * days
total_food = dog_food + cat_food + turtle_food
total_food_left = left_food - total_food

if total_food_left > 0:
    print(f"{floor(total_food_left)} kilos of food left.")
else:
    print(f"{ceil(abs(total_food_left))} more kilos of food are needed.")
