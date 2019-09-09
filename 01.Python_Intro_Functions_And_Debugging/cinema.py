projection = input()
rows = int(input())
columns = int(input())

seats = rows * columns

profit = None

if projection == 'Premiere':
    profit = seats * 12
elif projection == 'Normal':
    profit = seats * 7.5
elif projection == 'Discount':
    profit = seats * 5

print(f'{profit:.2f} leva')
