nums = list(map(int, input().split(' ')))

nums = list(filter(lambda x: x > 0, nums))

print(' '.join(map(str, nums[::-1])) if len(nums) > 0 else 'empty')
