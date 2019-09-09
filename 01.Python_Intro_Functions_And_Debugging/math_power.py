def get_power_of_number(number, power):
    return number ** power


if __name__ == '__main__':
    num = float(input())
    power_to_apply = float(input())

    print(get_power_of_number(num,power_to_apply))
