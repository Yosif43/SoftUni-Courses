months = int(input())

electricity_total = 0
for i in range(months):
    electricity = float(input())
    electricity_total += electricity

water_total = 20 * months
internet_total = 15 * months

other_total = (electricity_total + water_total + internet_total) * 1.2

total_expenses = electricity_total + water_total + internet_total + other_total
average_expenses = total_expenses / months

print(f"Electricity: {electricity_total:.2f} lv")
print(f"Water: {water_total:.2f} lv")
print(f"Internet: {internet_total:.2f} lv")
print(f"Other: {other_total:.2f} lv")
print(f"Average: {average_expenses:.2f} lv")