def make_honey(bees, nectar, symbols):
    total_honey = 0
    bees_left = []
    nectar_left = []

    while bees and nectar and symbols:
        bee = bees[0]
        nectar_value = nectar[0]
        symbol = symbols[0]

        if nectar_value >= bee:
            calculation_result = None

            if symbol == "+":
                calculation_result = abs(bee + nectar_value)
            elif symbol == "-":
                calculation_result = abs(bee - nectar_value)
            elif symbol == "*":
                calculation_result = abs(bee * nectar_value)
            elif symbol == "/":
                if nectar_value != 0:
                    calculation_result = abs(bee / nectar_value)
            if calculation_result is not None:
                total_honey += calculation_result

            bees.pop(0)
            nectar.pop(0)
            symbol.pop(0)
        else:
            bees_left.append(bee)
            nectar.pop(0)
    bees_left += bees
    nectar_left += nectar

    print(f"Total honey made: {total_honey}")
    if bees_left:
        print(f"Bees left: {', '.join(map(str, bees_left))}")
    if nectar_left:
        print(f"Nectar left: {', '.join(map(str, nectar_left))}")

bees = list(map(int, input().split()))
nectar = list(map(int, input().split()))
symbols = input().split()

make_honey(bees, nectar, symbols)