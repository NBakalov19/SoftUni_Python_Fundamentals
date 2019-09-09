money_needed = float(input())
money_saved = float(input())

counter = 0
spend_counter = 0
output = ''

while True:
    command = input()
    current_money = float(input())
    counter += 1

    if command == 'save':
        money_saved += current_money
        if money_saved >= money_needed:
            output = f'You saved the money for {counter} days.'
            break

        spend_counter = 0
    elif command == 'spend':
        spend_counter += 1

        if spend_counter == 5:
            output = f"You can't save the money.\n{counter}"
            break
        else:
            if money_saved > current_money:
                money_saved -= current_money
            else:
                money_saved = 0

print(output)
