holidays = int(input())

working_days = 365 - holidays

playtime_mins = working_days * 63 + holidays * 127
yearly_playtime_mins = 30000
result = 0

if playtime_mins <= yearly_playtime_mins:
    result = yearly_playtime_mins - playtime_mins
    hours = result // 60
    mins = result % 60
    print('Tom sleeps well')
    print(f'{hours} hours and {mins} minutes less for play')
else:
    result = playtime_mins - yearly_playtime_mins
    hours = result // 60
    mins = result % 60
    print('Tom will run away')
    print(f'{hours} hours and {mins} minutes more for play')
