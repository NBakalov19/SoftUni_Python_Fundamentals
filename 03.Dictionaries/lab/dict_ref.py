data_list = input().split(' = ')

names_dict = {}

while not data_list[0] == 'end':
    key = data_list[0]
    value = data_list[1]

    if data_list[1].isdigit():
        names_dict[key] = int(value)
    else:
        if value in names_dict.keys():
            names_dict[key] = names_dict[value]
    data_list = input().split(' = ')

for key, value in names_dict.items():
    print(f'{key} === {value}')
