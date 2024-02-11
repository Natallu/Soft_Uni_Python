windows = int(input())
windows_type = input()
delivery = input()

price_list = {
    "90X130": 110,
    "100X150": 140,
    "130X180": 190,
    "200X300": 250
}

discount = 0

if windows < 10:
    print("Invalid order")
    exit()

if windows_type == "90X130":

    if 30 < windows <= 60:
        discount = 0.05
    elif windows > 60:
        discount = 0.08

elif windows_type == "100X150":

    if 40 < windows <= 80:
        discount = 0.06
    elif windows > 80:
        discount = 0.1

elif windows_type == "130X180":

    if 20 < windows <= 50:
        discount = 0.07
    elif windows > 50:
        discount = 0.12

elif windows_type == "200X300":

    if 25 < windows <= 50:
        discount = 0.09
    elif windows > 50:
        discount = 0.14

total_cost = (windows * price_list[windows_type]) - (windows * price_list[windows_type]) * discount

if delivery == 'With delivery':
    total_cost += 60

if windows > 99:
    total_cost = total_cost - total_cost * 0.04

print(f"{total_cost:.2f} BGN")
