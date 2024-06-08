pages_amount = int(input())
pages_hour = int(input())
days = int(input())
pages_day = pages_amount // pages_hour
hours_day = pages_day // days

print(hours_day)
