from sys import maxsize

minimum = maxsize
data = 0

while data != 'Stop':
    data = input()
    if data == 'Stop':
        print(minimum)
        break
    else:
        data = int(data)
        if data < minimum:
            minimum = data
