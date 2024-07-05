budged = float(input())
season = input()

price = 0
location = ""
places = ""

if budged <= 1000:
    places = "Camp"
    if season == "Summer":
        location = "Alaska"
        price = budged * 0.65
    elif season == "Winter":
        location = "Morocco"
        price = budged * 0.45
elif 1000 < budged <= 3000:
    places = "Hut"
    if season == "Summer":
        location = "Alaska"
        price = budged * 0.80
    elif season == "Winter":
        location = "Morocco"
        price = budged * 0.60
elif budged > 3000:
    places = "Hotel"
    if season == "Summer":
        location = "Alaska"
        price = budged * 0.90
    elif season == "Winter":
        location = "Morocco"
        price = budged * 0.90

print(f"{location} - {places} - {price:.2f}")
