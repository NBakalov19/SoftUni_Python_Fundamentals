if __name__ == '__main__':

    lines = int(input())

    wardrobe_dict = {}

    for line in range(lines):
        dict_info = input().split(' -> ')

        color = dict_info[0]
        clothes = dict_info[1].split(',')

        if color not in wardrobe_dict.keys():
            wardrobe_dict[color] = {}

        for cloth in clothes:

            if cloth in wardrobe_dict[color]:
                wardrobe_dict[color][cloth] += 1
            else:
                wardrobe_dict[color][cloth] = 1

    cloth_to_found = input()

    for key, value in wardrobe_dict.items():
        print(f'{key} clothes:')
        for inner_key, inner_value in wardrobe_dict[key].items():
            curr_cloth = f'{key} {inner_key}'
            cloth_is_found = ' (found!)' if cloth_to_found == curr_cloth else ''
            print(f'* {inner_key} - {inner_value}{cloth_is_found}')
