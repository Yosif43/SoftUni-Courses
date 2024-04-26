players = {}


def add_player(player, position, skill):
    if player not in players:
        players[player] = {}

    if position not in players[player] or skill > players[player][position]:
        players[player][position] = skill


def duel_players(player1, player2):
    if player1 in players and player2 in players:
        common_positions = set(players[player1].keys()).intersection(set(players[player2].keys()))

        if common_positions:
            total_skill_player1 = sum(players[player1][position] for position in common_positions)
            total_skill_player2 = sum(players[player2][position] for position in common_positions)

            if total_skill_player1 > total_skill_player2:
                remove_player(player2)
            elif total_skill_player1 < total_skill_player2:
                remove_player(player1)


def remove_player(player):
    del players[player]


def print_players():
    sorted_players = sorted(players.items(), key=lambda x: (-sum(x[1].values()), x[0]))

    for player, positions in sorted_players:
        total_skill = sum(positions.values())
        print(f"{player}: {total_skill} skill")

        sorted_positions = sorted(positions.items(), key=lambda x: (-x[1], x[0]))

        for position, skill in sorted_positions:
            print(f"- {position} <::> {skill}")

while True:
    command = input()

    if command == "Season end":
        break

    if "->" in command:
        player, position, skill = command.split(" -> ")
        skill = int(skill)
        add_player(player, position, skill)
    elif "vs" in command:
        player1, player2 = command.split(" vs ")
        duel_players(player1, player2)

print_players()
