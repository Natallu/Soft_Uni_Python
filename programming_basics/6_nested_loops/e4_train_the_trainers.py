teachers = int(input())
data = input()

all_grades = 0
counter_all_grades = 0
while data != 'Finish':
    presentation_name = data

    current_presentation_grade = 0
    for grade in range(1, teachers + 1):

        current_grade = float(input())
        current_presentation_grade += current_grade
        all_grades += current_grade
        counter_all_grades += 1

    average_current_presentation = current_presentation_grade / teachers

    print(f'{presentation_name} - {average_current_presentation:.2f}.')

    data = input()

average_grade = all_grades / counter_all_grades
print(f"Student's final assessment is {average_grade:.2f}.")
