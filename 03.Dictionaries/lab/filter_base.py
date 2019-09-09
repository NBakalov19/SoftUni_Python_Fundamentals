def print_dict(collection, criteria):
    for key, value in collection.items():
        print(f'Name: {key}')
        print(f'{criteria}: {value}')
        print('=' * 20)


if __name__ == '__main__':

    age_dict = {}
    salary_dict = {}
    position_dict = {}

    input_data = input().split(' -> ')

    while not input_data[0] == 'filter base':

        name = input_data[0]
        second_param = input_data[1]

        if second_param.isdigit():
            age_dict[name] = second_param
        else:
            try:
                float(second_param)
                salary_dict[name] = float(second_param)
            except ValueError:
                position_dict[name] = second_param

        input_data = input().split(' -> ')

    filter_criteria = input()

    if filter_criteria == 'Age':
        print_dict(age_dict, filter_criteria)
    elif filter_criteria == 'Salary':
        print_dict(salary_dict, filter_criteria)
    else:
        print_dict(position_dict, filter_criteria)
