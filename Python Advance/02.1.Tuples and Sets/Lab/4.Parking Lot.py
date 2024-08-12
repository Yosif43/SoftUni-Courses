n = int(input())
parking_space = set()

for _ in range(n):
    direction, reg_number = input().split(", ")
    if direction == "IN":
        parking_space.add(reg_number)
    elif direction == "OUT":
        if reg_number in parking_space: #important without this might trow an error
            parking_space.remove(reg_number)
if parking_space:
    for car in parking_space:
        print(car)
else:
    print("Parking Lot is Empty")
