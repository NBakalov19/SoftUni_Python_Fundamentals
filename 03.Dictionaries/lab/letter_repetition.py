word = input()

symbol_dict = {symbol: word.count(symbol) for symbol in word}

for key, value in symbol_dict.items():
    print(f'{key} -> {value}')
