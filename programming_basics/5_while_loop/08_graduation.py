student_name = input()

counter = 0
total_grades = 0
fail_counter = 0

while True:
    grades = float(input())

    if grades < 4:
        fail_counter += 1

        if fail_counter > 1:
            years = counter + 1
            print(f'{student_name} has been excluded at {years} grade')
            break

        continue

    elif grades >= 4:
        total_grades += grades
        counter += 1

        if counter == 12:
            average_grade = total_grades / counter
            print(f'{student_name} graduated. Average grade: {average_grade:.2f}')
            break
