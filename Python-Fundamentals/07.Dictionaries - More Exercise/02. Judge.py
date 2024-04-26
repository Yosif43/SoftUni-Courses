def add_participant(contests, participants, username, contest, points):
    if contest not in contests:
        contests[contest] = {}

    if username not in contests[contest]:
        contests[contest][username] = 0

    contests[contest][username] = max(contests[contest][username], points)

    if username not in participants:
        participants[username] = 0

    participants[username] += points


def print_results(contests, participants):
    sorted_contests = sorted(contests.keys())

    for contest in sorted_contests:
        participants_count = len(contests[contest])
        print(f"{contest}: {participants_count} participants")

        sorted_participants = sorted(contests[contest].keys(), key=lambda x: (-contests[contest][x], x))
        for i, participant in enumerate(sorted_participants, start=1):
            points = contests[contest][participant]
            print(f"{i}. {participant} <::> {points}")

    print("Individual standings:")
    sorted_participants = sorted(participants.keys(), key=lambda x: (-participants[x], x))
    for i, participant in enumerate(sorted_participants, start=1):
        points = participants[participant]
        print(f"{i}. {participant} -> {points}")


contests = {}
participants = {}

while True:
    line = input()
    if line == "no more time":
        break

    username, contest, points = line.split(" -> ")
    points = int(points)

    add_participant(contests, participants, username, contest, points)

print_results(contests, participants)

