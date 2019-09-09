def is_in_range(collection: list, range_bound: int):
    in_range = True

    for element in collection:
        if element > range_bound - 1:
            in_range = False
            break

    return in_range


def get_taken_index(collection_of_indices: list, collection_of_elements: list):
    taken_index = None

    for index in collection_of_indices:
        if collection_of_elements[index] == -1:
            taken_index = index
            break

    return taken_index


if __name__ == '__main__':
    elements = list(map(int, input().split(', ')))

    indices_str = input()

    total_compounds = 0

    while not indices_str == 'end':
        indices = list(map(int, indices_str.split('-')))

        if is_in_range(indices, len(elements)):

            if get_taken_index(indices, elements) is None:
                found_compound_list = []

                for index in indices:
                    found_compound_list.append(elements[index])
                    elements[index] = -1

                total_compounds += 1
                print(f'Found compound: {found_compound_list}')

            else:
                tkn_index = get_taken_index(indices, elements)
                print(f'Index {tkn_index} already taken')

        else:
            print('Invalid indices')

        indices_str = input()

    print(f'Total compounds: {total_compounds}')
    elements_left = list(filter(lambda e: e != -1, elements))
    print(f'Elements left: {elements_left}')
