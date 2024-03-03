year = int(input())

while True:
    year += 1
    str_year = str(year)
    if len(str_year) == len(set(str_year)):
        print(year)
        break
