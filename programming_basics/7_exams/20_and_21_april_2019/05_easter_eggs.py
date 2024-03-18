total_eggs = int(input())

red_eggs = 0
orange_eggs = 0
blue_eggs = 0
green_eggs = 0

for _ in range(total_eggs):
    egg_color = input()

    if egg_color == "red":
        red_eggs += 1
    elif egg_color == "orange":
        orange_eggs += 1
    elif egg_color == "blue":
        blue_eggs += 1
    elif egg_color == "green":
        green_eggs += 1

max_color = max(red_eggs, orange_eggs, blue_eggs, green_eggs)

print(f"Red eggs: {red_eggs}")
print(f"Orange eggs: {orange_eggs}")
print(f"Blue eggs: {blue_eggs}")
print(f"Green eggs: {green_eggs}")
print(f"Max eggs: {max_color} -> ", end="")

if max_color == red_eggs:
    print("red")
elif max_color == orange_eggs:
    print("orange")
elif max_color == blue_eggs:
    print("blue")
elif max_color == green_eggs:
    print("green")
