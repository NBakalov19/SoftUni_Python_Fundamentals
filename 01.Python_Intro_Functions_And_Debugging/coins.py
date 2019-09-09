change = float(input())

coins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2]
coins_nominal = len(coins)

coins_change = 0

i = coins_nominal - 1

while i >= 0:
    while change >= coins[i]:
        change -= coins[i]
        coins_change += 1

    i -= 1

print(coins_change)
