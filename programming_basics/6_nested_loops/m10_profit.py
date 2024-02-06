one_lev = int(input())
two_leva = int(input())
five_leva = int(input())
sum_amount = int(input())

for i in range(0, one_lev + 1):
    for j in range(0, two_leva + 1):
        for l in range(0, five_leva + 1):
            if i * 1 + j * 2 + l * 5 == sum_amount:
                print(f"{i} * 1 lv. + {j} * 2 lv. + {l} * 5 lv. = {sum_amount} lv.")
