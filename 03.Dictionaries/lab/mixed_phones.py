data_input = input().split(' : ')

phone_book_dict = {}

while not data_input[0] == 'Over':

    first_element = data_input[0]
    second_element = data_input[1]

    if first_element.isdigit():
        phone_book_dict[second_element] = first_element
    else:
        phone_book_dict[first_element] = second_element

    data_input = input().split(' : ')

for key, value in sorted(phone_book_dict.items()):
    print(f'{key} -> {value}')
