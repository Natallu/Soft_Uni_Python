city = input()
sales = float(input())

comm = 0
valid_info = 'true'

if city == 'Sofia':
    if 0 <= sales <= 500:
        comm = 0.05 * sales
    elif 500 < sales <= 1000:
        comm = 0.07 * sales
    elif 1000 < sales <= 10000:
        comm = 0.08 * sales
    elif sales > 10000:
        comm = 0.12 * sales
    else:
        valid_info = not 'true'
elif city == 'Varna':
    if 0 <= sales <= 500:
        comm = 0.045 * sales
    elif 500 < sales <= 1000:
        comm = 0.075 * sales
    elif 1000 < sales <= 10000:
        comm = 0.1 * sales
    elif sales > 10000:
        comm = 0.13 * sales
    else:
        valid_info = not 'true'
elif city == 'Plovdiv':
    if 0 <= sales <= 500:
        comm = 0.055 * sales
    elif 500 < sales <= 1000:
        comm = 0.08 * sales
    elif 1000 < sales <= 10000:
        comm = 0.12 * sales
    elif sales > 10000:
        comm = 0.145 * sales
    else:
        valid_info = not 'true'
else:
    valid_info = not 'true'


if valid_info != 'true':
    print('error')
else:
    print(f'{comm:.2f}')
