town = input()
sells = float(input())
result = "error"

if town == "Sofia":
    if 0 <= sells <= 500:
        result = sells * 0.05
    elif 500 < sells <= 1000:
        result = sells * 0.07
    elif 1000 < sells <= 10000:
        result = sells * 0.08
    elif sells > 10000:
        result = sells * 0.12
elif town == "Varna":
    if 0 <= sells <= 500:
        result = sells * 0.045
    elif 500 < sells <= 1000:
        result = sells * 0.075
    elif 1000 < sells <= 10000:
        result = sells * 0.10
    elif sells > 10000:
        result = sells * 0.13
elif town == "Plovdiv":
    if 0 <= sells <= 500:
        result = sells * 0.055
    elif 500 < sells <= 1000:
        result = sells * 0.08
    elif 1000 < sells <= 10000:
        result = sells * 0.12
    elif sells > 10000:
        result = sells * 0.145
if result == "error":
    print(result)
else:
    print(f"{result:.2f}")
