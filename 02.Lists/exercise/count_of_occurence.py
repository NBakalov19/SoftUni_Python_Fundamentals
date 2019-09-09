if __name__ == '__main__':
    nums = list(map(int, input().split(' ')))

    new_list = list(set(nums))
    new_list.sort()

    for num in new_list:
        print(f'{num} -> {nums.count(num)}')
