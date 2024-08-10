from collections import deque

products = deque()
robots = []
robots_data = input().split(";")
hours, minutes, second = [int(x) for x in input().split(":")]
start_time_seconds = hours * 3600 + minutes * 60 + second

for robot in robots_data:
    robot_name, processing_time = robot.split("-")
    busy_until_time = 0
    robots.append({"name": robot_name, "data": [int(processing_time), busy_until_time]})

while True:
    product = input()
    if product == "End":
        break
    products.append(product)

while products:
    start_time_seconds += 1
    current_product = products.popleft()
    is_taken = False

    for robot in robots:
        if robot["data"][1] <= start_time_seconds:
            robot["data"][1] = start_time_seconds + robot["data"][0]
            h = start_time_seconds // 3600
            m = (start_time_seconds % 3600) // 60
            s = (start_time_seconds % 3600) % 60
            h %= 24
            print(f"{robot['name']} - {current_product} [{h:02d}:{m:02d}:{s:02d}]")
            is_taken = True
            break

    if not is_taken:
        products.append(current_product)
