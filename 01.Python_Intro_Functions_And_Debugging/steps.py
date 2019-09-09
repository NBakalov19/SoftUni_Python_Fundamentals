goal = 10000
steps_made = 0
diff = 0

while True:
    steps = input()

    if steps == 'Going home':
        steps_made += int(input())
        diff = goal - steps_made
        break
    steps_made += int(steps)

    if steps_made >= goal:
        break


if diff > 0:
    print(f'{diff} more steps to reach goal.')
else:
    print(f'Goal reached! Good job!')
