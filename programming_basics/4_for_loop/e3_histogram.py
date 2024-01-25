n = int(input())

p1, p2, p3, p4, p5 = 0, 0, 0, 0, 0

for num in range(n):
    number = int(input())
    if number < 200:
        p1 += 1
    elif 200 <= number <= 399:
        p2 += 1
    elif 400 <= number <= 599:
        p3 += 1
    elif 600 <= number <= 799:
        p4 += 1
    else:
        p5 += 1

percent1 = p1 / n * 100
percent2 = p2 / n * 100
percent3 = p3 / n * 100
percent4 = p4 / n * 100
percent5 = p5 / n * 100

print(f'{percent1:.2f}%')
print(f'{percent2:.2f}%')
print(f'{percent3:.2f}%')
print(f'{percent4:.2f}%')
print(f'{percent5:.2f}%')
