if __name__ == '__main__':
    data_list = input().split(':')

    company_dict = {}

    while not data_list[0] == 'ready':
        destination = data_list[0]
        vehicles = data_list[1].split(',')

        if destination not in company_dict.keys():
            company_dict[destination] = {}

        for vehicle in vehicles:
            type_vehicle = vehicle.split('-')[0]
            capacity = int(vehicle.split('-')[1])

            company_dict[destination][type_vehicle] = capacity

        data_list = input().split(':')

    groups_info = input().split()

    while not groups_info[0] == 'travel':
        group_destination = groups_info[0]
        group_count = int(groups_info[1])

        if group_count <= sum(company_dict[group_destination].values()):
            print(f'{group_destination} -> all {group_count} accommodated')
        else:
            not_accommodated_tourist = group_count - sum(company_dict[group_destination].values())
            print(f'{group_destination} -> all except {not_accommodated_tourist} accommodated')

        groups_info = input().split()
