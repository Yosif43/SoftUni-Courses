last_sector = input().strip()
initial_rows = int(input().strip())
odd_row_seats = int(input().strip())

total_seats = 0

for sector in range(ord('A'), ord(last_sector) + 1):
    rows_in_sector = initial_rows + (sector - ord('A'))
    for row in range(1, rows_in_sector + 1):
        if row % 2 == 1:
            seats_in_row = odd_row_seats
        else:
            seats_in_row = odd_row_seats + 2
        for seat in range(seats_in_row):
            seat_char = chr(ord('a') + seat)
            print(f"{chr(sector)}{row}{seat_char}")
            total_seats += 1

print(total_seats)
