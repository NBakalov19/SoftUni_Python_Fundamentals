if __name__ == '__main__':
    nums = list(map(int, input().split(' ')))

    smallest_element = nums[0]

    for num in nums:
        if num < smallest_element:
            smallest_element = num

    print(smallest_element)
