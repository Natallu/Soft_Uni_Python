most_powerful_word = ''
max_count = 0
vowels = ('a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y')

while True:
    text = input()

    if text == 'End of words':
        break

    word = text
    current_count = 0

    for char in word:
        current_count += ord(char)

    if word[0] in vowels:
        current_count = current_count * len(word)
    else:
        current_count = current_count // len(word)

    if current_count > max_count:
        max_count = current_count
        most_powerful_word = word

    current_count = 0

print(f"The most powerful word is {most_powerful_word} - {max_count}")
