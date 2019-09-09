data_list = input().split(' -> ')

names_dict = {}

while not data_list[0] == 'end':
    name = data_list[0]
    item = data_list[1].split(', ')

    if item[0].isdigit():
        if name not in names_dict.keys():
            names_dict[name] = []
        names_dict[name].extend(item)
    else:
        if item[0] in names_dict.keys():
            # if name not in names_dict.keys():
            #     names_dict[name] = []
            # names_dict[name].extend(names_dict[item[0]])
            names_dict[name] = names_dict[item[0]].copy()

    data_list = input().split(' -> ')

for key, value in names_dict.items():
    print(f"{key} === {', '.join(map(str, value))}")
