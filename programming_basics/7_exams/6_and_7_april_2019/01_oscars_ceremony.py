rent = int(input())

stats = rent - rent * 0.3
catt = stats - stats * 0.15
sound = catt / 2

expenses = stats + catt + sound + rent

print(f'{expenses:.2f}')
