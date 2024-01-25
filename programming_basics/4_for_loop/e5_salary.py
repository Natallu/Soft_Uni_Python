n_open_tabs = int(input())
salary = float(input())
tab = 0

for _ in range(n_open_tabs):
    tab = input()
    if tab == 'Facebook':
        salary -= 150
    elif tab == 'Instagram':
        salary -= 100
    elif tab == 'Reddit':
        salary -= 50

if salary <= 0:
    print('You have lost your salary.')
else:
    print(f'{salary:.0f}')
