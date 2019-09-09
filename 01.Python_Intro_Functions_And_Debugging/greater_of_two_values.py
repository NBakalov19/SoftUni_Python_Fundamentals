def get_greater(type_compare, first_value, second_value):
    output = None

    if type_compare == 'int':
        output = first_value if int(first_value) > int(second_value) else second_value
    else:
        output = first_value if first_value > second_value else second_value

    return output


if __name__ == '__main__':
    compare_type = input()
    value_one = input()
    value_two = input()

    print(get_greater(compare_type, value_one, value_two))
