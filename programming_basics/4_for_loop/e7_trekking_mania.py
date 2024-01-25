n_groups = int(input())

total_members = 0
musala, monblan, kilimanjaro, k2, everest = 0, 0, 0, 0, 0

for _ in range(n_groups):
    members = int(input())
    total_members += members
    if members <= 5:
        musala += members
    elif 6 <= members <= 12:
        monblan += members
    elif 13 <= members <= 25:
        kilimanjaro += members
    elif 26 <= members <= 40:
        k2 += members
    else:
        everest += members

musala_p = musala / total_members * 100
monblan_p = monblan / total_members * 100
kilimanjaro_p = kilimanjaro / total_members * 100
k2_p = k2 / total_members * 100
everest_p = everest / total_members * 100

print(f'{musala_p:.2f}%')
print(f'{monblan_p:.2f}%')
print(f'{kilimanjaro_p:.2f}%')
print(f'{k2_p:.2f}%')
print(f'{everest_p:.2f}%')
