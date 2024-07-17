n = int(input())
weights = []
total_weight = 0
microbus_weight = 0
truck_weight = 0
train_weight = 0

for i in range(n):
    w = int(input())
    weights.append(w)
    total_weight += w

for w in weights:
    if w <= 3:
        microbus_weight += w
    elif w <= 11:
        truck_weight += w
    else:
        train_weight += w

total_cost = microbus_weight * 200 + truck_weight * 175 + train_weight * 120

avg_cost = total_cost / total_weight

microbus_percent = microbus_weight / total_weight * 100
truck_percent = truck_weight / total_weight * 100
train_percent = train_weight / total_weight * 100

print(f"{avg_cost:.2f}")
print(f"{microbus_percent:.2f}%")
print(f"{truck_percent:.2f}%")
print(f"{train_percent:.2f}%")