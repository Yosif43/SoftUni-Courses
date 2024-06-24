gasoline_price = 2.22
diesel_price = 2.33
gas_price = 0.93

gasoline_liter_discount = 0.18
diesel_liter_discount = 0.12
gas_liter_discount = 0.08

fuel_type = input()
fuel_liters = float(input())
discount_card = input()

if fuel_type == "Diesel":
    if discount_card == "Yes":
        diesel_price = diesel_price - diesel_liter_discount
    else:
        diesel_price = 2.33
    if 20 <= fuel_liters <= 25:
        discount_percent = 8
    elif fuel_liters > 25:
        discount_percent = 10
    else:
        discount_percent = 0
    print(f"{fuel_liters * diesel_price - fuel_liters * diesel_price * discount_percent / 100:.2f} lv.")

if fuel_type == "Gas":
    if discount_card == "Yes":
        gas_price = gas_price - gas_liter_discount
    else:
        gas_price = 0.93
    if 20 <= fuel_liters <= 25:
        discount_percent = 8
    elif fuel_liters > 25:
        discount_percent = 10
    else:
        discount_percent = 0
    print(f"{fuel_liters * gas_price - fuel_liters * gas_price * discount_percent / 100:.2f} lv.")

if fuel_type == "Gasoline":
    if discount_card == "Yes":
        gasoline_price = gasoline_price - gasoline_liter_discount
    else:
        gasoline_price = 2.22
    if 20 <= fuel_liters <= 25:
        discount_percent = 8
    elif fuel_liters > 25:
        discount_percent = 10
    else:
        discount_percent = 0
    print(f"{fuel_liters * gasoline_price - fuel_liters * gasoline_price * discount_percent / 100:.2f} lv.")