n = int(input())
l = int(input())

end_index_of_first_l_letters = 97 + l

for first in range(1, n+1):
    for second in range(1, n+1):
        for third in range(97, end_index_of_first_l_letters):
            first_letter = chr(third)
            for fourth in range(97, end_index_of_first_l_letters):
                second_letter = chr(fourth)
                for fifth in range(1, n+1):
                    if fifth > first and fifth > second:
                        last_symbol = fifth
                        password = str(first) + str(second) + first_letter + second_letter + str(last_symbol)
                        print(password, end=" ")
