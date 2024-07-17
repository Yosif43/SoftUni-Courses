money = float(input())
up_to_year = int(input())

year_zero = 1800
money_per_year_even = 12000
money_per_year_odd = 12000 + 18 * 50
current_year = 0
expense = 0
for i in range(year_zero, up_to_year + 1):
    if i == 1800:
        expense = 12000
    elif i % 2 == 0:
        expense += 12000
    else:
        expense += 12000 + (18 + abs(1800 - i)) * 50

diff = abs(money - expense)

if expense <= money:
    print(f"Yes! He will live a carefree life and will have {diff:.2f} dollars left.")
else:
    print(f"He will need {diff:.2f} dollars to survive.")
