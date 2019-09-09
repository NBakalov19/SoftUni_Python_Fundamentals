nums = list(map(int, input().split(' ')))

for index in range(len(nums)):
    if index % 2 == 1 and nums[index] % 2 == 1:
        print(f'Index {index} -> {nums[index]}')
