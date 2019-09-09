trip_price = float(input())
sold_jigsaws = int(input())
sold_dolls = int(input())
sold_teddy_bears = int(input())
sold_minions = int(input())
sold_trucks = int(input())

jigsaw_price = 2.6
doll_price = 3
teddy_bear_price = 4.1
minion_price = 8.2
truck_price = 2

total_toys_sold = sold_dolls + sold_jigsaws + sold_minions + sold_teddy_bears + sold_trucks

total_price = (jigsaw_price * sold_jigsaws) + (doll_price * sold_dolls) + (teddy_bear_price * sold_teddy_bears) + (
        minion_price * sold_minions) + (truck_price * sold_trucks)

if total_toys_sold >= 50:
    total_price = 0.75 * total_price

total_price = total_price * 0.9

diff = max(total_price, trip_price) - min(total_price, trip_price)

print(f'Yes! {diff:.2f} lv left.' if total_price >= trip_price
      else f'Not enough money! {diff:.2f} lv needed.')
