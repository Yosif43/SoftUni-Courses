period = int(input())
doctors = 7
treated_patients = 0
untreated_patients = 0
count_days = 0
for i in range(0, period):
    count_days += 1
    patient = int(input())

    if count_days == 3:
        if untreated_patients > treated_patients:
            doctors += 1
        count_days = 0

    if patient > doctors:
        diff = patient - doctors  # 18 - 7 = 11
        treated_patients += doctors
        untreated_patients += diff
    elif patient <= doctors:
        treated_patients += patient

print(f'Treated patients: {treated_patients}.')
print(f'Untreated patients: {untreated_patients}.')
