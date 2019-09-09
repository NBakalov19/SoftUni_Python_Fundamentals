import math

figure = input()

area = None

if figure == 'square':
    side = float(input())
    area = side * side
elif figure == 'circle':
    radius = float(input())
    area = math.pi * radius ** 2
elif figure == 'triangle':
    first_side = float(input())
    height = float(input())
    area = first_side * height / 2
else:
    first_side = float(input())
    second_side = float(input())
    area = first_side * second_side

print(f'{area:.3f}')
