inventory_dict = {}

stock_data = input().split(' ')

while not stock_data[0] == 'shopping':

    stock = stock_data[1]
    quantity = int(stock_data[2])
    if stock in inventory_dict:
        inventory_dict[stock] += quantity
    else:
        inventory_dict[stock] = quantity

    stock_data = input().split(' ')

shop_item = input().split(' ')

while not shop_item[0] == 'exam':
    item = shop_item[1]
    item_quantity = int(shop_item[2])

    if item in inventory_dict:
        if inventory_dict[item] == 0:
            print(f'{item} out of stock')
        elif inventory_dict[item] > item_quantity:
            inventory_dict[item] -= item_quantity
        else:
            inventory_dict[item] = 0
    else:
        print(f'{item} doesn\'t exist')

    shop_item = input().split(' ')

for key, value in inventory_dict.items():
    if not value == 0:
        print(f'{key} -> {value}')
