number_sales = int(input())

hearthstone_counter = 0
fornite_counter = 0
overwatch_counter = 0
others_counter = 0


for game_name in range(number_sales):

    name = input()

    if name == 'Hearthstone':
        hearthstone_counter += 1
    elif name == 'Fornite':
        fornite_counter += 1
    elif name == 'Overwatch':
        overwatch_counter += 1
    else:
        others_counter += 1

hs_p = (hearthstone_counter / number_sales) * 100
fn_p = (fornite_counter / number_sales) * 100
ow_p = (overwatch_counter / number_sales) * 100
oe_p = (others_counter / number_sales) * 100

print(f'Hearthstone - {hs_p:.2f}%')
print(f'Fornite - {fn_p:.2f}%')
print(f'Overwatch - {ow_p:.2f}%')
print(f'Others - {oe_p:.2f}%')
