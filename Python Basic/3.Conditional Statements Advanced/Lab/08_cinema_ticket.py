day = input()
result = 0

if day == "Monday" or day == "Tuesday" or day == "Friday":
    result = 12
elif day == "Wednesday" or day == "Thursday":
    result = 14
elif day == "Saturday" or day == "Sunday":
    result = 16

print(result)
