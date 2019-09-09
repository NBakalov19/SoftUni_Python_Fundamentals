product = input()
town = input().lower()
quantity = float(input())

total_price = None

if town == 'sofia':
    if product == 'coffee':
        total_price = quantity * 0.5
    elif product == 'water':
        total_price = quantity * 0.8
    elif product == 'beer':
        total_price = quantity * 1.2
    elif product == 'sweets':
        total_price = quantity * 1.45
    elif product == 'peanuts':
        total_price = quantity * 1.6
elif town == 'plovdiv':
    if product == 'coffee':
        total_price = quantity * 0.4
    elif product == 'water':
        total_price = quantity * 0.7
    elif product == 'beer':
        total_price = quantity * 1.15
    elif product == 'sweets':
        total_price = quantity * 1.3
    elif product == 'peanuts':
        total_price = quantity * 1.5
elif town == 'varna':
    if product == 'coffee':
        total_price = quantity * 0.45
    elif product == 'water':
        total_price = quantity * 0.7
    elif product == 'beer':
        total_price = quantity * 1.1
    elif product == 'sweets':
        total_price = quantity * 1.35
    elif product == 'peanuts':
        total_price = quantity * 1.55

print(f'{total_price:.4f}')
