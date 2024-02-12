start = input()
end = input()

for x in range(int(start[0]), int(end[0]) + 1):
    for y in range(int(start[1]), int(end[1]) + 1):
        for j in range(int(start[2]), int(end[2]) + 1):
            for k in range(int(start[3]), int(end[3]) + 1):
                if x % 2 != 0 and y % 2 != 0 and j % 2 != 0 and k % 2 != 0:
                    barcode = f"{x}{y}{j}{k}"
                    print(barcode, end=" ")
