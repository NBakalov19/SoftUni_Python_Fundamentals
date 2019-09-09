import math

nums = list(map(int, input().split(' ')))
nums = list(filter(lambda num: math.sqrt(num) == int(math.sqrt(num)), nums))
nums.sort()
nums.reverse()

print(' '.join(map(str, nums)))
