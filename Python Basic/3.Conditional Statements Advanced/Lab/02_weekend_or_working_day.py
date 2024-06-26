day = input()
result = ""

if day == "Monday":
    result = "Working day"
elif day == "Tuesday":
    result = "Working day"
elif day == "Wednesday":
    result = "Working day"
elif day == "Thursday":
    result = "Working day"
elif day == "Friday":
    result = "Working day"
elif day == "Saturday":
    result = "Weekend"
elif day == "Sunday":
    result = "Weekend"
else:
    result = "Error"

print(result)
