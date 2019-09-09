def get_sign(number):
    output = ''
    if number > 0:
        output = f'The number {number} is positive.'
    elif number < 0:
        output = f'The number {number} is negative.'
    else:
        output = 'The number 0 is zero.'

    return output


if __name__ == '__main__':
    num = int(input())
    print(get_sign(num))
