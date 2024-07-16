from math import floor

count_games = int(input())
initial_scores = int(input())

F = 1200
W = 2000
SF = 720

average_scores = 0
count_win_games = 0

for i in range(count_games):
    position = input()

    if position == "F":
        initial_scores += F
        average_scores += F
    elif position == "W":
        initial_scores += W
        average_scores += W
        count_win_games += 1
    elif position == "SF":
        initial_scores += SF
        average_scores += SF

print(f"Final points: {initial_scores}")
print(f"Average points: {floor(average_scores / count_games)}")
print(f"{count_win_games / count_games * 100:.2f}%")
