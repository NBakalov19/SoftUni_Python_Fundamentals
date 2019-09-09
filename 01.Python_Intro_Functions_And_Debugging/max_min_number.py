number = input()

min_number = int(number)
max_number = int(number)

while not number == 'END':
    number = int(number)

    if number > max_number:
        max_number = number

    if number < min_number:
        min_number = number

    number = input()

print(f'Max number: {max_number}')
print(f'Min number: {min_number}')
