import re


def is_lower_case_word(value):
    if not value:
        return False

    for symbol in value:
        if not 'a' <= symbol <= 'z':
            return False

        if symbol == '':
            return False

    return True


def is_upper_case_word(value):
    if not value:
        return False

    for symbol in value:
        if not 'A' <= symbol <= 'Z':
            return False

    return True


if __name__ == '__main__':
    items = re.split('[,;:.!()\"\'\\\\/\\[\\]\\s]+', input())

    lower_case_items = []
    upper_case_items = []
    mixed_case_items = []

    for item in items:
        if is_lower_case_word(item):
            lower_case_items.append(item)
        elif is_upper_case_word(item):
            upper_case_items.append(item)
        else:
            if item:
                mixed_case_items.append(item)

print(f'Lower-case: ', end='')
print(', '.join(lower_case_items))
print(f'Mixed-case: ', end='')
print(', '.join(mixed_case_items))
print(f'Upper-case: ', end='')
print(', '.join(upper_case_items))
