def get_product_of_even_and_odd_sum(number_as_string):
    odd_sum = 0
    even_sum = 0

    for char in number_as_string:

        if not char.isdigit():
            continue
        else:
            digit = int(char)
            if digit % 2 == 0:
                even_sum += digit
            else:
                odd_sum += digit

    return odd_sum * even_sum


if __name__ == '__main__':
    number = input()

    print(get_product_of_even_and_odd_sum(number))
