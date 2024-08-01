line_input = input()
student_count = 0
standard_count = 0
kids_count = 0
total_count_tickets = 0

while line_input != "Finish":
    movie = line_input
    capacity = int(input())
    command_line = input()
    current_movie_count = 0

    while command_line != "End":
        type_ticket = command_line
        current_movie_count += 1
        total_count_tickets += 1

        if type_ticket == "student":
            student_count += 1
        elif type_ticket == "standard":
            standard_count += 1
        else:
            kids_count += 1

        if current_movie_count == capacity:
            break
        command_line = input()

    percentage_current = current_movie_count / capacity * 100
    print(f"{movie} - {percentage_current:.2f}% full.")
    line_input = input()

print(f"Total tickets: {total_count_tickets}")
percent_student = student_count / total_count_tickets * 100
percent_standard = standard_count / total_count_tickets * 100
percent_kids = kids_count / total_count_tickets * 100
print(f"{percent_student:.2f}% student tickets.")
print(f"{percent_standard:.2f}% standard tickets.")
print(f"{percent_kids:.2f}% kids tickets.")
