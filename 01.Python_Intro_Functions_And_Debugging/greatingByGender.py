age = float(input())
gender = input()

result = None

if age < 16:
    if gender == 'm':
        result = 'Master'
    elif gender == 'f':
        result = 'Miss'
else:
    if gender == 'm':
        result = 'Mr.'
    elif gender == 'f':
        result = 'Ms.'

print(result)
