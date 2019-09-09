items = input().split("|")

items.reverse()

new_items = []
for item in items:
    item = item.split()
    for el in item:
        new_items.append(el)

print(*new_items)
