import math

flowers_type = input()
flowers_count = int(input())
budget = int(input())

flowers = {
    "Roses": 5,
    "Dahlias": 3.8,
    "Tulips": 2.8,
    "Narcissus": 3,
    "Gladiolus": 2.5
}

money_needed = flowers_count * flowers[flowers_type]

discount = 0

if flowers_type == 'Roses' and flowers_count > 80:
    discount = 0.1 * money_needed
elif flowers_type == 'Dahlias' and flowers_count > 90:
    discount = 0.15 * money_needed
elif flowers_type == 'Tulips' and flowers_count > 80:
    discount = 0.15 * money_needed
elif flowers_type == 'Narcissus' and flowers_count < 120:
    discount = 0.15 * money_needed
elif flowers_type == 'Gladiolus' and flowers_count < 80:
    discount = 0.2 * money_needed

total_money_needed = money_needed

if flowers_type == 'Gladiolus' or flowers_type == 'Narcissus':
    total_money_needed = money_needed + discount
else:
    total_money_needed = money_needed - discount

difference = math.fabs(total_money_needed - budget)

if total_money_needed <= budget:
    print(f"Hey, you have a great garden with {flowers_count} {flowers_type} and {difference:.2f} leva left.")
else:
    print(f'Not enough money, you need {difference:.2f} leva more.')
