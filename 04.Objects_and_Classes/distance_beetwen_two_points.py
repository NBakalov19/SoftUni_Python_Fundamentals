import math


def calculate_distance(first_point, second_point):
    side_a = math.fabs(first_point.x - second_point.x)
    side_b = math.fabs(first_point.y - second_point.y)

    return math.sqrt(side_a ** 2 + side_b ** 2)


if __name__ == '__main__':
    class Point:
        def __init__(self, x, y):
            self.x = int(x)
            self.y = int(y)


    x, y = list(map(int, input().split()))

    first_point = Point(x, y)

    x, y = list(map(int, input().split()))
    second_point = Point(x, y)

    distance = calculate_distance(first_point, second_point)
    print(f'{distance:.3f}')
