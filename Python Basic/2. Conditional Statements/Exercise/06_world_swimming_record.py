import math

record = float(input())
distance = float(input())
swim_sec_per_meter = float(input())

requirements = distance * swim_sec_per_meter
sum_requirements = math.floor(distance / 15) * 12.5
total_time = requirements + sum_requirements


if total_time < record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {total_time - record:.2f} seconds slower.")
