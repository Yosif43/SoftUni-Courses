def accommodate_new_pets(capacity, max_weight, *pets):
    result = []
    pets_map = {}

    for pet_type, pet_weight in pets:
        if capacity <= 0:
            result.append("You did not manage to accommodate all pets!")
            break
        if pet_weight > max_weight:
            continue
        if pet_type not in pets_map:
            pets_map[pet_type] = 0
        pets_map[pet_type] += 1
        capacity -= 1
    else:
        result.append(f"All pets are accommodated! Available capacity: {capacity}.")

    result.append("Accommodated pets:")
    for pet_type, pet_count in sorted(pets_map.items()):
        result.append(f"{pet_type}: {pet_count}")
#or [result.append(f"{pet_type}: {pet_count}") for pet_type, pet_count in sorted(pets_map.items())]
    return "\n".join(result)





print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))
print()
print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))
print()
print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))