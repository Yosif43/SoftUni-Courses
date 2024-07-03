exam_hour = int(input())
exam_min = int(input())
arrival_hour = int(input())
arrival_min = int(input())

exam_hour_in_min = exam_hour * 60
arrival_hour_in_min = arrival_hour * 60

exam_all_min = exam_hour_in_min + exam_min
arrival_all_min = arrival_hour_in_min + arrival_min

diff = abs(arrival_all_min - exam_all_min)

if arrival_all_min > exam_all_min:
    print("Late")
    if diff < 60:
        print(f"{diff} minutes after the start")
    else:
        hours = diff // 60
        minutes = diff % 60
        if minutes < 10:
            print(f"{hours}:0{minutes} hours after the start")
        else:
            print(f"{hours}:{minutes} hours after the start")
elif arrival_all_min == exam_all_min or diff <= 30:
    print("On time")
    if 1 <= diff <= 30:
        print(f"{diff} minutes before the start")
else:
    print("Early")
    if diff < 60:
        print(f"{diff} minutes before the start")
    else:
        hours = diff // 60
        minutes = diff % 60
        if minutes < 10:
            print(f"{hours}:0{minutes} hours before the start")
        else:
            print(f"{hours}:{minutes} hours before the start")