size = int(input())
directions = input().split(", ")

hazelnuts = 0
s_row = 0
s_col = 0
is_game_over = False
direction_mapper = {"up": (-1, 0),
                    "down": (1, 0),
                    "left": (0, -1),
                    "right": (0, 1)} # not using the mapper in that solution
matrix = []

for row in range(size):
    matrix.append(list(input()))# when you have ready list in the input
    for col in range(size):
        if matrix[row][col] == "s": # that is the position of the squirel
            s_row = row
            s_col = col # assigning the position of "s" to s row and col

for direction in directions:
    matrix[s_row][s_col] = "*"

    if direction == "up":
        s_row -= 1
    elif direction == "down":
        s_row += 1
    elif direction == "left":
        s_col -= 1
    elif direction == "right":
        s_col += 1

    if not (0 <= s_row < size and 0 <= s_col < size): # this if is to check if squirel is going out of our matrix
        print("The squirrel is out of the field.")
        is_game_over = True
        break
    if matrix[s_row][s_col] == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        is_game_over = True
        break
    if matrix[s_row][s_col] == "h":
        hazelnuts += 1
        if hazelnuts == 3: # we know the total of hazelnuts will be in total 3 all the time
            is_game_over = True
            print("Good job! You have collected all hazelnuts!")
            break

if hazelnuts < 3 and not is_game_over:
    print("There are more hazelnuts to collect.")
print(f"Hazelnuts collected: {hazelnuts}")



"""" 
inputs 
 5
left, left, up, right, up, up
**h**
t****
*h***
*h*s*
*****

second input 
4
down, down, right, right
*s*h
***h
***t
h***

third input
4
down, down, right, right
h***
***h
*s*t
**h*
 """