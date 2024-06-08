amount_nylon = int(input())
amount_paint = int(input())
amount_paint_thinner = int(input())
worker_hours = int(input())

nylon_per_meter = 1.50
price_liter_paint = 14.50
price_liter_paint_thinner = 5.00
price_bags = 0.40
sum_nylon = (amount_nylon + 2) * nylon_per_meter
sum_paint = (amount_paint + (amount_paint * 10/100)) * price_liter_paint
sum_thinner = amount_paint_thinner * price_liter_paint_thinner

total_sum = sum_nylon + sum_paint + sum_thinner + price_bags
total_sum_workers = (total_sum * 30/100) * worker_hours

print(total_sum + total_sum_workers)