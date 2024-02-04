limit_one = int(input())
limit_two = int(input())
limit_three = int(input())

for i in range(1, limit_one + 1):
    if i % 2 == 0:
        first_number = i

        for j in range(1, limit_two + 1):

            if j == 2 or j == 3 or j == 5 or j == 7:
                second_number = j

                for k in range(1, limit_three + 1):

                    if k % 2 == 0:
                        third_number = k

                        print(f'{first_number} {second_number} {third_number}')
