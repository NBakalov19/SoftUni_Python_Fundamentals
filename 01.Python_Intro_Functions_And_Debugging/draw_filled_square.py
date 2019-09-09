def print_top_or_bottom_of_dashes(n):
    print(''.join('-' * (2 * n)))


def print_filling(n):
    print(''.join('\\/' * (n - 1)), end='')


def print_body(n):
    for row in range(1, n - 1):
        print('-', end='')
        print_filling(n)
        print('-', end='')
        print()


def print_square(n):
    print_top_or_bottom_of_dashes(n)
    print_body(n)
    print_top_or_bottom_of_dashes(n)


if __name__ == '__main__':
    size = int(input())
    print_square(size)
