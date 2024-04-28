from collections import defaultdict

dragons = defaultdict(lambda: {'damage': [], 'health': [], 'armor': []})

n = int(input())

for _ in range(n):
    dragon_info = input().split()
    type_name = dragon_info[0]
    name = dragon_info[1]
    damage = int(dragon_info[2]) if dragon_info[2] != 'null' else 45
    health = int(dragon_info[3]) if dragon_info[3] != 'null' else 250
    armor = int(dragon_info[4]) if dragon_info[4] != 'null' else 10

    dragons[type_name][name] = {'damage': damage, 'health': health, 'armor': armor}
    dragons[type_name]['damage'].append(damage)
    dragons[type_name]['health'].append(health)
    dragons[type_name]['armor'].append(armor)

for type_name, type_data in dragons.items():
    avg_damage = sum(type_data['damage']) / len(type_data['damage'])
    avg_health = sum(type_data['health']) / len(type_data['health'])
    avg_armor = sum(type_data['armor']) / len(type_data['armor'])

    print(f"{type_name}::({avg_damage:.2f}/{avg_health:.2f}/{avg_armor:.2f})")

    sorted_dragons = sorted(type_data.items(), key=lambda x: x[0])
    for dragon_name, dragon_stats in sorted_dragons:
        if dragon_name != 'damage' and dragon_name != 'health' and dragon_name != 'armor':
            print(
                f"-{dragon_name} -> damage: {dragon_stats['damage']}, health: {dragon_stats['health']}, armor: {dragon_stats['armor']}")
