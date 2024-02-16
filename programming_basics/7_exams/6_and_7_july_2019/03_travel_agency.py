city = input()
package = input()
discount_package = input()
days = int(input())

if days > 7:
    days = days - 1

price = 0
wrong_data = False

if city == 'Bansko' or city == 'Borovets':
    if package == 'withEquipment':
        price = days * 100
        if discount_package == 'yes':
            price = price - price * 0.1
        elif discount_package == 'no':
            price = price
    elif package == 'noEquipment':
        price = days * 80
        if discount_package == 'yes':
            price = price - price * 0.05
        elif discount_package == 'no':
            price = price
    else:
        wrong_data = True

elif city == 'Varna' or city == 'Burgas':
    if package == 'withBreakfast':
        price = days * 130
        if discount_package == 'yes':
            price = price - price * 0.12
        elif discount_package == 'no':
            price = price
    elif package == 'noBreakfast':
        price = days * 100
        if discount_package == 'yes':
            price = price - price * 0.07
        elif discount_package == 'no':
            price = price
    else:
        wrong_data = True

else:
    wrong_data = True

if days < 1:
    print("Days must be positive number!")
elif wrong_data == False:
    print(f'The price is {price:.2f}lv! Have a nice time!')
elif wrong_data:
    print('Invalid input!')
