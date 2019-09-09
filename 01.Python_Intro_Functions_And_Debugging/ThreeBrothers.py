import math

first_brother_time = float(input())
second_brother_time = float(input())
third_brother_time = float(input())
father_absence = float(input())

time_need_for_cleaning = 1 / ((1 / first_brother_time) + (1 / second_brother_time) + (1 / third_brother_time))

time_for_rest = 0.15 * time_need_for_cleaning

total_time = time_need_for_cleaning + time_for_rest

print(f'{total_time:.2f}')

difference_in_times = max(total_time, father_absence) - min(total_time, father_absence)

if total_time < father_absence:
    print(f'Yes, there is a surprise - time left -> {math.floor(difference_in_times)} hours.')
else:
    print(f"No, there isn't a surprise - shortage of time -> {math.ceil(difference_in_times)} hours.")
