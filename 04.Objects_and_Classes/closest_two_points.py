import math

if __name__ == '__main__':
    class Point:
        def __init__(self, x, y):
            self.x = int(x)
            self.y = int(y)

        def get_info(self):
            return f'{self.x}, {self.y}'


    class Segment:
        def __init__(self, first_point: Point, second_point: Point):
            self.first_point = first_point
            self.second_point = second_point
            self.distance = self.calculate_distance()

        def calculate_distance(self):
            side_a = abs(self.first_point.x - self.second_point.x)
            side_b = abs(self.first_point.y - self.second_point.y)

            return math.sqrt(side_a ** 2 + side_b ** 2)

        def get_info(self):
            return f'{self.distance:.3f}\n({self.first_point.get_info()})\n({self.second_point.get_info()})'


    lines = int(input())

    points_list = []

    for line in range(lines):
        x, y = input().split()
        point = Point(x, y)

        points_list.append(point)

    segment_list = []

    for index in range(len(points_list)):
        for inner_index in range(index + 1, len(points_list)):
            segment = Segment(points_list[index], points_list[inner_index])

            segment_list.append(segment)

    for segment in sorted(segment_list, key=lambda s: s.distance):
        print(segment.get_info())
        break
