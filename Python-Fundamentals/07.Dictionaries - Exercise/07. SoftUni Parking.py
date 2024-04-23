# import sys
#
# def validate_parking(n, commands):
#     registered_users = {}
#
#     for i in range(n):
#         command = commands[i].split()
#         action = command[0]
#
#         if action == "register":
#             username = command[1]
#             license_plate = command[2]
#
#             if username in registered_users:
#                 print(f"ERROR: already registered with plate number {registered_users[username]}")
#             else:
#                 registered_users[username] = license_plate
#                 print(f"{username} registered {license_plate} successfully")
#
#         elif action == "unregister":
#             username = command[1]
#
#             if username not in registered_users:
#                 print(f"ERROR: user {username} not found")
#             else:
#                 license_plate = registered_users.pop(username)
#                 print(f"{username} unregistered successfully")
#
#     for username, license_plate in registered_users.items():
#         print(f"{username} => {license_plate}")
#
# n = int(sys.stdin.readline().strip())
# commands = []
# for _ in range(n):
#     commands.append(sys.stdin.readline().strip())
#
# validate_parking(n, commands)

