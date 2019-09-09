cup_volume = int(input())

filled_water = 0
counter = 0

while filled_water < cup_volume:
    button_pressed = input()

    if button_pressed == 'Easy':
        counter += 1
        filled_water += 50
    elif button_pressed == 'Medium':
        counter += 1
        filled_water += 100
    elif button_pressed == 'Hard':
        counter += 1
        filled_water += 200

diff = filled_water - cup_volume
output = ''
if diff == 0:
    output = f'The dispenser has been tapped {counter} times.'
else:
    output = f'{diff}ml has been spilled.'

print(output)
