from math import floor

u_x1, u_y1, u_x2, u_y2 = float(input()), float(input()), float(input()), float(input())


def calculate_distance(def_x1, def_y1, def_x2, def_y2):
    return (def_x2 - def_x1) ** 2 + (def_y2 - def_y1) ** 2


dist_x1y1 = calculate_distance(u_x1, u_y1, 0, 0)
dist_x2y2 = calculate_distance(u_x2, u_y2, 0, 0)

if dist_x1y1 > dist_x2y2:
    print(tuple([floor(u_x2), floor(u_y2)]))
elif dist_x1y1 <= dist_x2y2:
    print(tuple([floor(u_x1), floor(u_y1)]))