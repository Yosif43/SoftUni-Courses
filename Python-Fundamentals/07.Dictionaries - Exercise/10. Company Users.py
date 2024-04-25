companies = {}
command = input().split(" -> ")
while command[0] != "End":
    company, employee = command
    if company not in companies.keys():
        companies[company] = []
    if employee not in companies[company]:
        companies[company].append(employee)
    command = input().split(" -> ")
for company, employees in companies.items():
    print(company)
    for employee in employees:
        print(f"-- {employee}")
