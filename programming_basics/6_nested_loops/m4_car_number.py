start_range = int(input())
end_range = int(input())

for first in range(start_range, end_range + 1):
    for second in range(start_range, end_range + 1):
        for third in range(start_range, end_range + 1):
            for fourth in range(start_range, end_range + 1):
                sum_result = second + third
                car_number = ''
                if first > fourth and sum_result % 2 == 0:
                    if ((first % 2 == 0 and fourth % 2 != 0) or
                            (first % 2 != 0 and fourth % 2 == 0)):
                        car_number = f'{first}{second}{third}{fourth}'
                        print(car_number, end=' ')
