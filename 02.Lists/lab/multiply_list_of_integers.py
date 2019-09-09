def multiply(element, multiplier):
    return element * multiplier


if __name__ == '__main__':
    data_list = list(map(int, input().split(' ')))
    num = int(input())

    numbers_list = [multiply(el, num) for el in data_list]

# print(*numbers_list)

    print(' '.join(map(str, numbers_list)))
