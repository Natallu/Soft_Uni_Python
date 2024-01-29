book_name = input()
book_counter = 0

while True:
    current_book = input()
    if current_book != book_name and current_book != 'No More Books':
        book_counter += 1
    elif current_book == 'No More Books':
        print('The book you search is not here!')
        print(f'You checked {book_counter} books.')
        break

    elif current_book == book_name:
        print(f'You checked {book_counter} books and found it.')
        break
