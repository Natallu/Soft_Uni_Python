n_number = int(input())

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for l in range(1, 10):
                first = i + j
                second = k + l
                if first == second and n_number % first == 0:
                    lucky_number = f'{i}{j}{k}{l}'
                    print(lucky_number, end=" ")
