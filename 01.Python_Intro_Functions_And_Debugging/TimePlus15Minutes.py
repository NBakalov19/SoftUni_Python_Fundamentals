hours = int(input())
minutes = int(input())

total_time_in_minutes = (hours * 60) + minutes

time_after_15_minutes = total_time_in_minutes + 15

hours = time_after_15_minutes // 60
minutes = time_after_15_minutes % 60

minutes = '0' + str(minutes) if minutes < 10 else minutes

print(f'{hours}:{minutes}')
