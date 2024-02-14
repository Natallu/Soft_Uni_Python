data = input()

total_tickets = 0
student_tickets = 0
kids_tickets = 0
standard_tickets = 0

while data != 'Finish':
    current_movie = data
    available_seats = int(input())

    input_line = input()
    current_tickets_counter = 0
    while input_line != 'End':
        ticket_type = input_line
        current_tickets_counter += 1
        total_tickets += 1

        if input_line == 'student':
            student_tickets += 1
        elif input_line == 'standard':
            standard_tickets += 1
        elif input_line == 'kid':
            kids_tickets += 1

        if current_tickets_counter == available_seats:
            break

        input_line = input()

    hall_p = (current_tickets_counter / available_seats) * 100

    print(f"{current_movie} - {hall_p:.2f}% full.")

    data = input()

students_p = (student_tickets / total_tickets) * 100
kids_p = (kids_tickets / total_tickets) * 100
standard_p = (standard_tickets / total_tickets) * 100
print(f'Total tickets: {total_tickets}')
print(f'{students_p:.2f}% student tickets.')
print(f'{standard_p:.2f}% standard tickets.')
print(f'{kids_p:.2f}% kids tickets.')
