capacity = int(input())
all_fans = int(input())

sector_a, sector_b, sector_v, sector_g = 0, 0, 0, 0

for _ in range(all_fans):

    current_fan = input()
    if current_fan == 'A':
        sector_a += 1
    elif current_fan == 'B':
        sector_b += 1
    elif current_fan == 'V':
        sector_v += 1
    elif current_fan == 'G':
        sector_g += 1

percent_a = sector_a / all_fans * 100
percent_b = sector_b / all_fans * 100
percent_v = sector_v / all_fans * 100
percent_g = sector_g / all_fans * 100
percent_fans_capacity = all_fans / capacity * 100

print(f'{percent_a:.2f}%')
print(f'{percent_b:.2f}%')
print(f'{percent_v:.2f}%')
print(f'{percent_g:.2f}%')
print(f'{percent_fans_capacity:.2f}%')
