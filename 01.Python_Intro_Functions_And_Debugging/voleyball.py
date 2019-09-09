import math

year_type = input()
celebrity_days = int(input())
days_in_village = int(input())

weekends = 48

games_in_sofia = 0.75 * (weekends - days_in_village)
games_on_celebrity_days = (2 / 3) * celebrity_days

total_games = games_in_sofia + games_on_celebrity_days + days_in_village

if year_type == 'leap':
    total_games = total_games + (0.15 * total_games)

print(math.floor(total_games))
