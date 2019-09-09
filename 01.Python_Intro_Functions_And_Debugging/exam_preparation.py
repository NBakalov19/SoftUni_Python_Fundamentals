count_of_bad_grades = int(input())

bad_grades = 0
average_grades = 0
task_count = 0
last_task = ''
output = ''

while True:
    command = input()
    if command == 'Enough':
        average_grades /= task_count
        output = f'Average score: {average_grades:.2f}\n' \
            f'Number of problems: {task_count}\n' \
            f'Last problem: {last_task}'

        break
    task_name = command
    grade = int(input())

    last_task = task_name
    task_count += 1
    average_grades += grade

    if grade <= 4:
        bad_grades += 1
        if bad_grades == count_of_bad_grades:
            output = f'You need a break, {count_of_bad_grades} poor grades.'
            break

print(output)
