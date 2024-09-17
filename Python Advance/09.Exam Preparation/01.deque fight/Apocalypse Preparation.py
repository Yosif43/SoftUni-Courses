from collections import deque

textiles = deque([int(el) for el in input().split()])
medicaments = list(int(el) for el in input().split())

items = {"Patch": 0, "Bandage": 0, "MedKit": 0}
med_kid_cost = 100
bandage_cost = 40
patch_cost = 30

while textiles and medicaments:
    current_textile = textiles.popleft()
    current_medicament = medicaments.pop()
    total_sum = current_medicament + current_textile
    if total_sum >= med_kid_cost:
        items["MedKit"] += 1
        if total_sum > 100:
            total_sum -= 100
            medicaments[-1] += total_sum
    elif total_sum == bandage_cost:
        items["Bandage"] += 1
    elif total_sum == patch_cost:
        items["Patch"] += 1
    elif total_sum != items["MedKit"] or total_sum != items["Patch"] or total_sum != items["Bandage"]:
        medicaments.append(current_medicament)
        medicaments[-1] += 10


if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")

for item, amount in sorted(items.items(), key=lambda x: (-x[1], x[0])):
    if amount > 0:
        print(f"{item} - {amount}")


if textiles:
    print("Textiles left:", ", ".join(map(str, textiles)))
elif medicaments:
    medicaments.reverse()
    print("Medicaments left:", ", ".join(map(str, medicaments)))


