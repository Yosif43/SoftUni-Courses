budged = float(input())
season = input()

car_type = ""
class_type = ""
price = 0

if budged <= 100:
    class_type = "Economy class"
    if season == "Summer":
        car_type = "Cabrio"
        price = budged * 0.35
    elif season == "Winter":
        car_type = "Jeep"
        price = budged * 0.65
elif 100 < budged <= 500:
    class_type = "Compact class"
    if season == "Summer":
        car_type = "Cabrio"
        price = budged * 0.45
    elif season == "Winter":
        car_type = "Jeep"
        price = budged * 0.80
elif budged > 500:
    class_type = "Luxury class"
    if season == "Summer" or season == "Winter":
        car_type = "Jeep"
        price = budged * 0.90

print(class_type)
print(f"{car_type} - {price:.2f}")
