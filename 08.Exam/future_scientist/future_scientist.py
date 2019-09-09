import math

if __name__ == '__main__':
    days_to_complete_courses = int(input())
    courses_count = int(input())
    hours_per_course = int(input())

    learning_hours = 0
    needed_hours = courses_count * hours_per_course

    for day in range(1, days_to_complete_courses + 1):

        if day % 2 == 0:
            learning_hours += 4
        elif day % 5 == 0:
            learning_hours += 2
        else:
            learning_hours += 1

    if learning_hours >= needed_hours:
        hours_left = learning_hours - needed_hours
        print(f'You watched all the courses and are left with {hours_left} free hours')
    else:
        diff = needed_hours - learning_hours
        count_incomplete_courses = diff / hours_per_course
        print(f'You need to complete {math.ceil(count_incomplete_courses)} more courses')
