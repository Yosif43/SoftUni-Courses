pieces = {}
n = int(input())

for _ in range(n):
    piece_info = input().split("|")
    piece = piece_info[0]
    composer = piece_info[1]
    key = piece_info[2]
    pieces[piece] = {"composer": composer, "key": key}

command = input()
while command != "Stop":
    command = command.split("|")
    action = command[0]
    piece = command[1]

    if action == "Add":
        composer = command[2]
        key = command[3]
        if piece in pieces:
            print(f"{piece} is already in the collection!")
        else:
            pieces[piece] = {"composer": composer, "key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif action == "Remove":
        if piece in pieces:
            del pieces[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif action == "ChangeKey":
        new_key = command[2]
        if piece in pieces:
            pieces[piece]["key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    command = input()

for piece, info in pieces.items():
    composer = info["composer"]
    key = info["key"]
    print(f"{piece} -> Composer: {composer}, Key: {key}")
