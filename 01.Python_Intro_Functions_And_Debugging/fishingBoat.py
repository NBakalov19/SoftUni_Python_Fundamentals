import math

budget = int(input())
season = input()
fishermans_count = int(input())

rent_price = {
    'Spring': 3000,
    'Summer': 4200,
    'Autumn': 4200,
    'Winter': 2600
}

price = rent_price[season]

discount = 0

if fishermans_count <= 6:
    discount = 0.1 * price
elif 6 < fishermans_count <= 11:
    discount = 0.15 * price
else:
    discount = 0.25 * price

total_price = price - discount
if fishermans_count % 2 == 0 and season != 'Autumn':
    total_price = total_price * 0.95

difference = math.fabs(budget - total_price)

if total_price > budget:
    print(f'Not enough money! You need {difference:.2f} leva.')
else:
    print(f'Yes! You have {difference:.2f} leva left.')
