number = int(input())
statement = 0

if 100 <= number <= 200 or number == 0:
    statement = 'true'
else:
    statement = not 'true'
    print('invalid')
