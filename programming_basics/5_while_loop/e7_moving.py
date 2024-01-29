width = int(input())
length = int(input())
height = int(input())

total_space = width * length * height
space = 0

data = input()
while data != 'Done':
    current_boxes = int(data)
    space += current_boxes

    if space >= total_space:
        break

    data = input()

diff = total_space - space
if space > total_space:
    print(f"No more free space! You need {abs(diff)} Cubic meters more.")
elif space <= total_space:
    print(f"{abs(diff)} Cubic meters left.")
