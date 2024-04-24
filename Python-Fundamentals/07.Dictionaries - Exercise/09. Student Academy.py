# students_count = int(input())
# students = {}
#
# for _ in range(students_count):
#     name = input()
#     grade = float(input())
#
#     if name not in students:
#         students[name] = []
#
#     students[name].append(grade)
#
# filtered_students = {name: sum(grades) / len(grades) for name, grades in students.items() if sum(grades) / len(grades) >= 4.50}
#
# for name, average_grade in filtered_students.items():
#     print(f"{name} -> {average_grade:.2f}")
#
#
