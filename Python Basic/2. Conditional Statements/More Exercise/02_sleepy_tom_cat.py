days_off = int(input())

year_minutes = 30000
play_off_days = days_off * 127
working_days = (365 - days_off)
working_days_minutes = working_days * 63
total_minutes = (play_off_days + working_days_minutes)
hours_left = abs(year_minutes - total_minutes) // 60
minutes_left = abs(year_minutes - total_minutes) % 60


if year_minutes > total_minutes:
    print("Tom sleeps well")
    print(f"{hours_left} hours and {minutes_left} minutes less for play")
else:
    print("Tom will run away")
    print(f"{hours_left} hours and {minutes_left} minutes more for play")
