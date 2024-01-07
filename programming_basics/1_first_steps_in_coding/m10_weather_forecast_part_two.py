temperature = float(input())

if 5.0 <= temperature <= 11.9:
    print('Cold')
elif 12.0 <= temperature <= 14.9:
    print('Cool')
elif 15.0 <= temperature <= 20.0:
    print('Mild')
elif 20.1 <= temperature <= 25.9:
    print('Warm')
elif 26.0 <= temperature <= 35.0:
    print('Hot')
else:
    print('unknown')
