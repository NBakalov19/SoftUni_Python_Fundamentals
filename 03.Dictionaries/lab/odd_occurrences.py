data_list = input().lower().split(' ')

odd_dict = {}

for word in data_list:
    odd_dict[word] = data_list.count(word)

# dictionary comprehension from list
# oct_dict = {word: data_list.count(word) for word in data_list}

result = []

for key, value in odd_dict.items():
    if value % 2 == 1:
        result.append(key)

print(', '.join(map(str, result)))
