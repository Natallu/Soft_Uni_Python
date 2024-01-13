day_of_the_week = input()

if day_of_the_week in ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'):
    print('Working day')
elif day_of_the_week == 'Saturday' or day_of_the_week == 'Sunday':
    print('Weekend')
else:
    print('Error')
