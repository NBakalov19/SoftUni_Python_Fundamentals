import math

if __name__ == '__main__':
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __str__(self):
            return f'{self.x}, {self.y}'

        @staticmethod
        def calculate_distance(first_point, second_point):
            side_a = abs(first_point.x - second_point.x)
            side_b = abs(first_point.y - second_point.y)

            return math.sqrt(side_a ** 2 + side_b ** 2)


    class Box:
        def __init__(self, upper_left: Point, upper_right: Point, bottom_left: Point, bottom_right: Point):
            self.upper_left = upper_left
            self.upper_right = upper_right
            self.bottom_left = bottom_left
            self.bottom_right = bottom_right
            self.width = Point.calculate_distance(self.upper_left, self.upper_right)
            self.height = Point.calculate_distance(self.upper_left, self.bottom_left)

        def calculate_perimeter(self):
            return (2 * self.width) + (2 * self.height)

        def calculate_area(self):
            return self.width * self.height

        def __str__(self):
            return f'Box: {self.width:.0f}, {self.height:.0f}\n' + \
                   f'Perimeter: {self.calculate_perimeter():.0f}\n' + \
                   f'Area: {self.calculate_area():.0f}'


    def create_point(item: str):
        x, y = [int(num) for num in item.split(':')]
        point = Point(x, y)

        return point


    def create_box(up_l, up_r, bt_l, bt_r):
        upper_left = create_point(up_l)
        upper_right = create_point(up_r)
        bottom_left = create_point(bt_l)
        bottom_right = create_point(bt_r)

        return Box(upper_left, upper_right, bottom_left, bottom_right)


    data_list = input().split(' | ')
    box_list = []

    while not data_list[0] == 'end':
        box = create_box(data_list[0], data_list[1], data_list[2], data_list[3])
        box_list.append(box)

        data_list = input().split(' | ')

    for box in box_list:
        print(box)
