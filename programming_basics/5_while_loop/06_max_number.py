from sys import maxsize

maximum = - maxsize
data = 0

while data != 'Stop':
    data = input()
    if data == 'Stop':
        print(maximum)
        break
    else:
        data = int(data)
        if data > maximum:
            maximum = data
