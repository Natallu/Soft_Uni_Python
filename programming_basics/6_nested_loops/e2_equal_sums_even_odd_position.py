first_number = int(input())
second_number = int(input())

for number in range(first_number, second_number + 1):
    position_of_number = str(number)

    even_sum = 0
    odd_sum = 0

    for i in range(0, len(position_of_number)):
        current_number = int(position_of_number[i])

        if i % 2 == 0:
            even_sum += current_number
        else:
            odd_sum += current_number

    if even_sum == odd_sum:
        print(position_of_number, end=" ")
