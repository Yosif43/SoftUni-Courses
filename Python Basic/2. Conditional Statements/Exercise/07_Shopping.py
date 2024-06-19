budged = float(input())
gpu = int(input())
cpu = int(input())
ram = int(input())

price_gpu = 250
total_price_gpu = price_gpu * gpu
price_cpu = total_price_gpu * 35 / 100
total_price_cpu = cpu * price_cpu
price_ram = total_price_gpu * 10 / 100
total_price_ram = ram * price_ram
total_sum = total_price_gpu + total_price_cpu + total_price_ram

if gpu > cpu:
    total_sum *= 85 / 100

budged_left = abs(budged - total_sum)

if budged >= total_sum:
    print(f"You have {budged_left:.2f} leva left!")
else:
    print(f"Not enough money! You need {budged_left:.2f} leva more!")
