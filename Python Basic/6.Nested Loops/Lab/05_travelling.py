while True:
    destination = input()

    if destination == "End":
        break

    exc_price = float(input())
    curr_money = 0

    while curr_money < exc_price:
        curr_money += float(input())

    print(f"Going to {destination}!")


