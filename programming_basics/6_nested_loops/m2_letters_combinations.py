first_letter = input()
second_letter = input()
third_letter = input()

start_interval = ord(first_letter)
end_interval = ord(second_letter)
exclude = ord(third_letter)
count = 0
a, b, c = 0, 0, 0
for first_ in range(start_interval, end_interval + 1):

    if first_ == exclude:
        continue
    else:
        a = first_

    for second_ in range(start_interval, end_interval + 1):

        if second_ == exclude:
            continue
        else:
            b = second_

        for third_ in range(start_interval, end_interval + 1):

            if third_ == exclude:
                continue
            else:
                c = third_
            count += 1
            combination = f'{chr(a)}{chr(b)}{chr(c)}'

            print(f'{combination}', end=" ")

print(f'{count}')
