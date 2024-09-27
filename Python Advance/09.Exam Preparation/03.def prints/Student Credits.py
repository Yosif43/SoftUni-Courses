def students_credits(*courses_data):
    courses_credits = []

    total_credits = 0

    for course_data in courses_data:
        course_name, credits, max_points, diyan_points = course_data.split('-')
        credits, max_points, diyan_points = int(credits), int(max_points), int(diyan_points)
        diyan_credits = (diyan_points / max_points) * credits
        courses_credits.append((course_name, diyan_credits))
        total_credits += diyan_credits

    courses_credits.sort(key=lambda x: x[1], reverse=True)

    if total_credits >= 240:
        result = f"Diyan gets a diploma with {total_credits:.1f} credits.\n"
    else:
        result = f"Diyan needs {240 - total_credits:.1f} credits more for a diploma.\n"

    for course, credit in courses_credits:
        result += f"{course} - {credit:.1f}\n"

    return result.strip()


print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)
print()
print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)
print()
print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)