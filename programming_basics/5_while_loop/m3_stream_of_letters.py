data = input()
word = ""
new_word = ""
count_c = 0
count_o = 0
count_n = 0
while data != "End":
    if 'a' <= data <= 'z' or 'A' <= data <= 'Z':
        if data == 'n' and count_n == 0:
            count_n += 1
        elif data == 'c' and count_c == 0:
            count_c += 1
        elif data == 'o' and count_o == 0:
            count_o += 1
        else:
            word += data

        if count_n == 1 and count_c == 1 and count_o == 1:
            new_word = new_word + word + " "

            word = ""
            count_n = 0
            count_c = 0
            count_o = 0

    data = input()

print(new_word)
