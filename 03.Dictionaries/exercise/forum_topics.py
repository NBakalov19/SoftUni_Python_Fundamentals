if __name__ == '__main__':

    data_list = input().split(' -> ')

    forum_dict = {}

    while not data_list[0] == 'filter':
        topic = data_list[0]
        tags_list = data_list[1].split(', ')

        if topic not in forum_dict.keys():
            forum_dict[topic] = []

        forum_dict[topic].extend([tag for tag in tags_list if tag not in forum_dict[topic]])

        data_list = input().split(' -> ')

    tags_to_find = input().split(', ')

    for key, value in forum_dict.items():
        are_existing_tags = all(elem in value for elem in tags_to_find)

        if are_existing_tags:
            value = list(map(lambda v: '#' + v, value))
            print(f"{key} | {', '.join(map(str, value))}")
