vero = int(input()) * 750
counter = 0
vero_needed = 0
pots = 0
plates = 0

input_line = input()
while input_line != "End":
    dishes = int(input_line)
    if dishes == int(input_line):
        counter += 1

    if counter % 3 == 0:
        pots += dishes
        vero_needed += dishes * 15
    else:
        plates += dishes
        vero_needed += dishes * 5

    if vero_needed > vero:
        break

    input_line = input()

diff = abs(vero - vero_needed)
if vero_needed <= vero:
    print("Detergent was enough!")
    print(f"{plates} dishes and {pots} pots were washed.")
    print(f"Leftover detergent {diff} ml.")
else:
    print(f"Not enough detergent, {diff} ml. more necessary!")