def fill_the_box(*args):
    box_volume = args[0] * args[1] * args[2]
    cubes = 0
    for item in args[3:]:
        if item == "Finish":
            break
        cubes += item
    if box_volume > cubes:
        return f"There is free space in the box. You could put {box_volume - cubes} more cubes."
    return f"No more free space! You have {cubes - box_volume} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print()
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print()
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
