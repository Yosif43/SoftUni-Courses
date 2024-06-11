w_wide = float(input())
h_high = float(input())

hallway = 1

w_wide = w_wide * 100
h_high = (h_high - hallway) * 100

workplace_w = w_wide // 120
workplace_h = h_high // 70


total_places = workplace_w * workplace_h - 3

print(f"{total_places:.2f}")
