def get_triangle_area(triangle_side, triangle_height):
    area = (triangle_side * triangle_height) / 2

    return '{:.12g}'.format(area)


if __name__ == '__main__':
    side = float(input())
    height = float(input())

    print(get_triangle_area(side, height))
