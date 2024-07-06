season = input()
group_type = input()
amount_students = int(input())
amount_nights = int(input())

price = 0
sport = ""

if season == "Winter":
    if group_type == "boys":
        sport = "Judo"
        price = amount_students * 9.60 * amount_nights
    elif group_type == "girls":
        sport = "Gymnastics"
        price = amount_students * 9.60 * amount_nights
    elif group_type == "mixed":
        sport = "Ski"
        price = amount_students * 10 * amount_nights
elif season == "Spring":
    if group_type == "boys":
        sport = "Tennis"
        price = amount_students * 7.20 * amount_nights
    elif group_type == "girls":
        sport = "Athletics"
        price = amount_students * 7.20 * amount_nights
    elif group_type == "mixed":
        sport = "Cycling"
        price = amount_students * 9.50 * amount_nights
elif season == "Summer":
    if group_type == "boys":
        sport = "Football"
        price = amount_students * 15 * amount_nights
    elif group_type == "girls":
        sport = "Volleyball"
        price = amount_students * 15 * amount_nights
    elif group_type == "mixed":
        sport = "Swimming"
        price = amount_students * 20 * amount_nights

if amount_students >= 50:
    price = price - price * 0.50
elif 20 <= amount_students < 50:
    price = price - price * 0.15
elif 10 <= amount_students < 20:
    price = price - price * 0.05

print(f"{sport} {price:.2f} lv.")
