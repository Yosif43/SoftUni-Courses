cm_long = int(input())
cm_wide = int(input())
cm_high = int(input())
percent = float(input())

aquarium_size = cm_long * cm_wide * cm_high
aquarium_in_liters = aquarium_size * 0.001
liters_need = aquarium_in_liters * (1 - (percent / 100))

print(liters_need)
