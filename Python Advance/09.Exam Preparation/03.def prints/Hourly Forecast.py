def forecast(*args):
    sunny = sorted([loc for loc in args if loc[1] == "Sunny"], key=lambda x: x[0])
    cloudy = sorted([loc for loc in args if loc[1] == "Cloudy"], key=lambda x: x[0])
    rainy = sorted([loc for loc in args if loc[1] == "Rainy"], key=lambda x: x[0])

    sorted_locations = sunny + cloudy + rainy
    return "\n".join([f"{loc[0]} - {loc[1]}" for loc in sorted_locations])

print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
print()
print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
print()
print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))