name = input()

year = 1
average_grade = 0

while year <= 12:
    grade = float(input())

    if grade >= 4:
        year += 1
        average_grade += grade

average_grade /= 12

print(f'{name} graduated. Average grade: {average_grade:.2f}')
