numbers_list = list(map(float, input().split(' ')))

occ_dict = {num: numbers_list.count(num) for num in numbers_list}

for key, value in sorted(occ_dict.items()):
    # msg = 'times' if value > 1 else 'time'
    print(f'{key} -> {value} times')
