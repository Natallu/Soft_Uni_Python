failed_threshold = int(input())

failed_assignments_counter = 0
assignments_counter = 0
grades_counter = 0

while failed_assignments_counter < failed_threshold:
    current_assignment_name = input()

    if current_assignment_name == 'Enough':
        average_grade = grades_counter / assignments_counter
        print(f"Average score: {average_grade:.2f}")
        print(f"Number of problems: {assignments_counter}")
        print(f"Last problem: {assignment_name}")
        break

    grade_received = int(input())
    assignments_counter += 1
    grades_counter += grade_received
    assignment_name = 0
    assignment_name = current_assignment_name

    if grade_received <= 4:
        failed_assignments_counter += 1
        if failed_assignments_counter >= failed_threshold:
            print(f"You need a break, {failed_assignments_counter} poor grades.")
            break
