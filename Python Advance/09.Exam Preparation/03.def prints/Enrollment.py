def gather_credits(needed_credits, *courses):
    enrolled_courses = set()
    gathered_credits = 0

    for course in courses:
        course_name, course_credits = course
        if course_name in enrolled_courses:
            continue

        gathered_credits += course_credits
        enrolled_courses.add(course_name)

        if gathered_credits >= needed_credits:
            break

    if gathered_credits >= needed_credits:
        courses_sorted = ", ".join(sorted(enrolled_courses))
        return f"Enrollment finished! Maximum credits: {gathered_credits}.\nCourses: {courses_sorted}"
    else:
        credits_shortage = needed_credits - gathered_credits
        return f"You need to enroll in more courses! You have to gather {credits_shortage} credits more."


print(gather_credits(
    80,
    ("Basics", 27),
))
print()
print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))
print()
print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))
