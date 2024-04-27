def dict_details(our_dict, name, color, power):
    if color not in our_dict.keys():
        our_dict[color] = {}
    if name not in our_dict[color].keys():
        our_dict[color][name] = power
    else:
        if our_dict[color][name] < power:
            our_dict[color][name] = power
    return our_dict


dwarfs_details = {}

information = input()

while information != "Once upon a time":
    name, color_of_hat, physics = information.split(" <:> ")

    dwarfs_details = dict_details(dwarfs_details, name, color_of_hat, int(physics))

    information = input()

list_of_dwarfs = []

for hat_color, dwarfs_list in dwarfs_details.items():
    for name, power in dwarfs_list.items():
        list_of_dwarfs.append({"name": name, "physics": power, "hat": hat_color, "dwarfs_num": len(dwarfs_list)})

for item in sorted(list_of_dwarfs, key=lambda x: (-x["physics"], -x["dwarfs_num"])):
    print(f"({item['hat']}) {item['name']} <-> {item['physics']}")

#
# or
#
# from collections import Counter
#
# command = input()
# dwarfs_by_hat = {}
#
# while command != "Once upon a time":
#     name, hat, physics = command.split(" <:> ")
#     physics = int(physics)
#     dwarfs_by_hat.setdefault(hat, {})
#     dwarfs_by_hat[hat][name] = max(physics, dwarfs_by_hat[hat].get(name, 0))
#     command = input()
#
# result = []
# for color, names in dwarfs_by_hat.items():
#     for name, value in names.items():
#         result.append((color, name, value))
#
# hat_counts = Counter(color for color, _, _ in result)
# result = sorted(result, key=lambda x: (-x[2], -hat_counts[x[0]]))
#
# for color, name, value in result:
#     print(f"({color}) {name} <-> {value}")