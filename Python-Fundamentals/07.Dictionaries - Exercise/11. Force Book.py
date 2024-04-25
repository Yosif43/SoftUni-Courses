force_users = {}

while True:
    command = input()
    if command == "Lumpawaroo":
        break

    if " | " in command:
        force_side, force_user = command.split(" | ")
        if force_user not in force_users:
            if force_side not in force_users:
                force_users[force_side] = []
            force_users[force_side].append(force_user)
    elif " -> " in command:
        force_user, force_side = command.split(" -> ")
        if force_user not in force_users:
            if force_side not in force_users:
                force_users[force_side] = []
            force_users[force_side].append(force_user)
            
            print(f"{force_user} joins the {force_side} side!")

for force_side, users in force_users.items():
    if users:
        print(f"Side: {force_side}, Members: {len(users)}")
        for user in users:
            print(f"! {user}")


