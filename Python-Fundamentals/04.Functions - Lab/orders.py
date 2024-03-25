def check(order_type: str, qty: int):
    if order_type == "coffee":
        return 1.5 * qty
    elif order_type == "coke":
        return 1.4 * qty
    elif order_type == "water":
        return 1 * qty
    elif order_type == "snacks":
        return 2 * qty


order = input()
quantity = int(input())
total_bill = check(order, quantity)
print(f"{total_bill:.2f}")