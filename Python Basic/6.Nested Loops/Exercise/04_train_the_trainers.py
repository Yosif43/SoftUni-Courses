people_assessment = int(input())

line_input = input()

count_grades = 0
sum_all_grades = 0
while line_input != "Finish":
    presentation = line_input

    sum_current_grade_avg = 0
    for i in range(1, people_assessment + 1):
        current_grade = float(input())
        count_grades += 1
        sum_all_grades += current_grade
        sum_current_grade_avg += current_grade
    avg_grade_current = sum_current_grade_avg / people_assessment
    print(f"{presentation} - {avg_grade_current:.2f}.")

    line_input = input()

final_avg_grade = sum_all_grades / count_grades
print(f"Student's final assessment is {final_avg_grade:.2f}.")