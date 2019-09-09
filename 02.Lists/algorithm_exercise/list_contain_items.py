if __name__ == '__main__':
    nums = list(map(int, input().split(' ')))
    num_to_found = int(input())

    isFound = False

    for num in nums:
        if num == num_to_found:
            isFound = True
            break

    print('yes' if isFound else 'no')