import math

income_per_person = float(input())
average_grade = float(input())
minimum_salary = float(input())

if average_grade >= 4.5:
    if average_grade >= 5.5:
        social_scholarship = 0.35 * minimum_salary
        excellent_result_scholarship = average_grade * 25
        scholarship = None
        if social_scholarship > excellent_result_scholarship and income_per_person < minimum_salary:
            scholarship = social_scholarship
            print(f'You get a Social scholarship {math.floor(scholarship)} BGN')
        else:
            scholarship = excellent_result_scholarship
            print(f'You get a scholarship for excellent results {math.floor(scholarship)} BGN')

    elif income_per_person < minimum_salary:
        scholarship = 0.35 * minimum_salary
        print(f'You get a Social scholarship {math.floor(scholarship)} BGN')
    else:
        print('You cannot get a scholarship!')
else:
    print('You cannot get a scholarship!')
