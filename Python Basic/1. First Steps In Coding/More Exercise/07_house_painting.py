x_high = float(input())
y_long = float(input())
h_triangle_high = float(input())

sidewall = x_high * y_long
window = 1.5 * 1.5
door = 1.2 * 2
both_sidewall = (sidewall * 2) - (window * 2)
backwall = x_high * x_high
frontwall = backwall - door
green = (both_sidewall + backwall + frontwall) / 3.4

roofsides = 2 * sidewall
rooftriangle = 2 * (x_high * h_triangle_high / 2)

red = (rooftriangle + roofsides) / 4.3

print(f"{green:.2f}")
print(f"{red:.2f}")
