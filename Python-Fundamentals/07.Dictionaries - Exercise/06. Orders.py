products = {}
command = input().split()
while command[0] != "buy":
    product_name, price, quantity = command[0], float(command[1]), int(command[2])
    if product_name not in products.keys():
        products[product_name] =[price, quantity]
    else:
        products[product_name][0] = price
        products[product_name][1] += quantity

    command = input().split()
for key, value in products.items():
    total_price = value[0] * value[1]
    print(f"{key} -> {total_price:.2f}")
