nums = list(map(int, input().split(' ')))

print(len(list(filter(lambda el: el % 2 == 1, nums))))
