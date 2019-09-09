if __name__ == '__main__':
    nums = list(map(int, input().split(' ')))

    for index in range(len(nums) // 2):
        first_element = nums[0 + index]
        last_element = nums[-1 - index]
        nums[index] = last_element
        nums[-1 - index] = first_element

    print(*nums)
