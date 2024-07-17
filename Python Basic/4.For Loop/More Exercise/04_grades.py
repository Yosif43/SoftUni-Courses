students_count = int(input())
grades = []

for _ in range(students_count):
    grade = float(input())
    grades.append(grade)

top_students = len([grade for grade in grades if grade >= 5])
between_4_and_5 = len([grade for grade in grades if 4 <= grade <= 4.99])
between_3_and_4 = len([grade for grade in grades if 3 <= grade <= 3.99])
fail_students = len([grade for grade in grades if grade < 3])

average_grade = sum(grades) / students_count

print(f"Top students: {top_students / students_count * 100:.2f}%")
print(f"Between 4.00 and 4.99: {between_4_and_5 / students_count * 100:.2f}%")
print(f"Between 3.00 and 3.99: {between_3_and_4 / students_count * 100:.2f}%")
print(f"Fail: {fail_students / students_count * 100:.2f}%")
print(f"Average: {average_grade:.2f}")