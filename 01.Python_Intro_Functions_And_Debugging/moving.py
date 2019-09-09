width = int(input())
length = int(input())
height = int(input())

apartment_volume = width * length * height
volume_taken = 0
output = ''

while True:
    command = input()
    if command == 'Done':
        break

    boxes_count = int(command)
    volume_taken += boxes_count

    if volume_taken > apartment_volume:
        break

diff = volume_taken - apartment_volume

if diff <= 0:
    output = f'{diff * -1} Cubic meters left.'
else:
    output = f'No more free space! You need {diff} Cubic meters more.'

print(output)
