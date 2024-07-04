junior_cyclists = int(input())
senior_cyclists = int(input())
trail_ground = input()

total_sum = 0

if trail_ground == "trail":
    total_sum = (junior_cyclists * 5.50) + (senior_cyclists * 7)
    total_sum *= 0.95
elif trail_ground == "cross-country":
    if junior_cyclists + senior_cyclists >= 50:
        total_sum = (junior_cyclists * 8) + (senior_cyclists * 9.50)
        total_sum *= 0.75
        total_sum *= 0.95
    else:
        total_sum = (junior_cyclists * 8) + (senior_cyclists * 9.50)
        total_sum *= 0.95
elif trail_ground == "downhill":
    total_sum = (junior_cyclists * 12.25) + (senior_cyclists * 13.75)
    total_sum *= 0.95
elif trail_ground == "road":
    total_sum = (junior_cyclists * 20) + (senior_cyclists * 21.50)
    total_sum *= 0.95

print(f"{total_sum:.2f}")
