if __name__ == '__main__':
    class Rectangle:
        def __init__(self, left, top, width, height):
            self.left = left
            self.top = top
            self.width = width
            self.height = height
            self.right = self.get_right()
            self.bottom = self.get_bottom()

        def get_right(self):
            return self.left + self.width

        def get_bottom(self):
            return self.top + self.height


    def is_inside(first_rectangle: Rectangle, second_rectangle: Rectangle):
        return first_rectangle.left >= second_rectangle.left \
               and first_rectangle.right <= second_rectangle.right \
               and first_rectangle.top <= second_rectangle.top \
               and first_rectangle.bottom <= second_rectangle.bottom


    left, top, width, height = list(map(int, input().split()))
    rectangle_one = Rectangle(left=left, top=top, width=width, height=height)

    left, top, width, height = list(map(int, input().split()))
    rectangle_two = Rectangle(left=left, top=top, width=width, height=height)

    print('Inside' if is_inside(rectangle_one, rectangle_two) else 'Not inside')
