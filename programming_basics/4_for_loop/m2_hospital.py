days = int(input())

doctors = 7
t_patients = 0
unt_patients = 0
day_counter = 0

for current_day in range(days):
    current_day_count = int(input())
    day_counter += 1
    if day_counter == 3:
        day_counter = 0
        if unt_patients > t_patients:
            doctors += 1

    if current_day_count <= doctors:
        t_patients += current_day_count
    else:
        t_patients += doctors
        unt_patients += current_day_count - doctors

print(f'Treated patients: {t_patients}.')
print(f'Untreated patients: {unt_patients}.')
