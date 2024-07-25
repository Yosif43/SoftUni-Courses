width = int(input())
length = int(input())

no_more_pieces = False
count_pieces = width * length

input_line = input()
while input_line != 'STOP':
    current_pieces = int(input_line)
    count_pieces -= current_pieces

    if count_pieces <= 0:
        no_more_pieces = True
        break

    input_line = input()

if no_more_pieces:
    print(f"No more cake left! You need {abs(count_pieces)} pieces more.")
else:
    print(f"{count_pieces} pieces are left.")