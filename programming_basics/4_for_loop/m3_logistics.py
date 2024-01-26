count_transfers = int(input())

van = 0
truck = 0
train = 0
total_tons = 0
total_price = 0

for _ in range(count_transfers):
    transfer_tons = int(input())
    total_tons += transfer_tons
    if transfer_tons <= 3:
        van += transfer_tons
        total_price += transfer_tons * 200
    elif 4 <= transfer_tons <= 11:
        truck += transfer_tons
        total_price += transfer_tons * 175
    else:
        train += transfer_tons
        total_price += transfer_tons * 120

average_price = total_price / total_tons
van_percent = van / total_tons * 100
truck_percent = truck / total_tons * 100
train_percent = train / total_tons * 100

print(f'{average_price:.2f}')
print(f'{van_percent:.2f}%')
print(f'{truck_percent:.2f}%')
print(f'{train_percent:.2f}%')
