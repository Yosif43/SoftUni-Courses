age = float(input())
gender = input()

if gender == 'm':
    if age >= 16:
        result = 'Mr.'
    else:
        result = 'Master'
elif gender == 'f':
    if age >= 16:
        result = "Ms."
    else:
        result = "Miss"

print(result)