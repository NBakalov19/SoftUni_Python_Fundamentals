favorite_book = input()
count_of_books = int(input())
counter = 0
output = ''

while True:
    current_book = input()
    if current_book == favorite_book:
        output = f'You checked {counter} books and found it.'
        break

    counter += 1

    if counter == count_of_books:
        output = f'The book you search is not here!\n' \
            f'You checked {counter} books.'
        break

print(output)
