fruit = input()
day = input()
price = float(input())
result = "error"

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    if fruit == "banana":
        result = price * 2.50
    elif fruit == "apple":
        result = price * 1.20
    elif fruit == "orange":
        result = price * 0.85
    elif fruit == "grapefruit":
        result = price * 1.45
    elif fruit == "kiwi":
        result = price * 2.70
    elif fruit == "pineapple":
        result = price * 5.50
    elif fruit == "grapes":
        result = price * 3.85
elif day == "Saturday" or day == "Sunday":
    if fruit == "banana":
        result = price * 2.70
    elif fruit == "apple":
        result = price * 1.25
    elif fruit == "orange":
        result = price * 0.90
    elif fruit == "grapefruit":
        result = price * 1.60
    elif fruit == "kiwi":
        result = price * 3.00
    elif fruit == "pineapple":
        result = price * 5.60
    elif fruit == "grapes":
        result = price * 4.20
if result == "error":
    print(result)
else:
    print(f"{result:.2f}")


