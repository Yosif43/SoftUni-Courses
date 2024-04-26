contests = {}

while True:
    line = input()
    if line == "end of contests":
        break
    contest, password = line.split(":")
    contests[contest] = password

users = {}

while True:
    line = input()
    if line == "end of submissions":
        break
    contest, password, username, points = line.split("=>")
    points = int(points)

    if contest in contests and contests[contest] == password:
        if username not in users:
            users[username] = {}
        if contest not in users[username]:
            users[username][contest] = points
        else:
            users[username][contest] = max(users[username][contest], points)

users_points = {user: sum(points.values()) for user, points in users.items()}

best_candidate = max(users_points, key=users_points.get)
total_points = users_points[best_candidate]
print(f"Best candidate is {best_candidate} with total {total_points} points.")
print("Ranking:")
sorted_users = sorted(users.keys())

for user in sorted_users:
    print(user)
    sorted_contests = sorted(users[user], key=users[user].get, reverse=True)
    for contest in sorted_contests:
        points = users[user][contest]
        print(f"#  {contest} -> {points}")
