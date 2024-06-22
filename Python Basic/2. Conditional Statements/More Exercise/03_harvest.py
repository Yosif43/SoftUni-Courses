import math

grape_square_field = int(input())
grape_per_square = float(input())
liters_wine = int(input())
workers = int(input())

total_grapes = grape_square_field * grape_per_square

grapes_for_wine = total_grapes * 0.40

wine_produced = grapes_for_wine / 2.5

if wine_produced < liters_wine:
    wine_needed = liters_wine - wine_produced
    print(f"It will be a tough winter! More {math.floor(wine_needed)} liters wine needed.")
else:
    total_wine = math.floor(wine_produced)
    wine_left = wine_produced - liters_wine
    wine_per_worker = wine_left / workers
    print(f"Good harvest this year! Total wine: {total_wine} liters.")
    print(f"{math.ceil(wine_left)} liters left -> {math.ceil(wine_per_worker)} liters per person.")
