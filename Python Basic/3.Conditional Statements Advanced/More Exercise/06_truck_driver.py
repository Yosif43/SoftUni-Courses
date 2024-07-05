season = input()
kilometers = float(input())

wages = 0
tax = 0

if kilometers <= 5000:
    if season == "Spring" or season == "Autumn":
        wages = kilometers * 0.75
        wages *= 4
    elif season == "Summer":
        wages = kilometers * 0.90
        wages *= 4
    elif season == "Winter":
        wages = kilometers * 1.05
        wages *= 4
elif 5000 < kilometers <= 10000:
    if season == "Spring" or season == "Autumn":
        wages = kilometers * 0.95
        wages *= 4
    elif season == "Summer":
        wages = kilometers * 1.10
        wages *= 4
    elif season == "Winter":
        wages = kilometers * 1.25
        wages *= 4
elif 10000 < kilometers <= 20000:
    if season == "Spring" or season == "Autumn" or season == "Summer" or season == "Winter":
        wages = kilometers * 1.45
        wages *= 4

tax = wages - wages * 0.10
print(f"{tax:.2f}")
