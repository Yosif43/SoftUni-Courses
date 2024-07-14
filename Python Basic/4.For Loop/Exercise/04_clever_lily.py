age = int(input())
washing_machine_price = float(input())
price_per_toy = int(input())

saved_money = 0
number_of_toys = 0
money_for_birthday = 10

for current_year in range(1, age + 1):
    if current_year % 2 == 0:
        saved_money += (money_for_birthday - 1)
        money_for_birthday += 10
    else:
        number_of_toys += 1

saved_money += number_of_toys * price_per_toy

diff = abs(saved_money - washing_machine_price)
if saved_money >= washing_machine_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
