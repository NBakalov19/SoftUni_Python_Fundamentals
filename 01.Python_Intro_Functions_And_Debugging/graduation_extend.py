name = input()

year = 1
average_grade = 0
not_passed_year = 0
result = ''

while year <= 12:
    grade = float(input())

    if grade >= 4:
        year += 1
        average_grade += grade
    else:
        not_passed_year += 1
        if not_passed_year > 1:
            result = f'{name} has been excluded at {year} grade'
            break

average_grade /= 12

if result == '':
    result = f'{name} graduated. Average grade: {average_grade:.2f}'

print(result)
