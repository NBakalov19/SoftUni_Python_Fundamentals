import math

if __name__ == '__main__':
    shells_dict = {}

    tokens = input().split(' ')

    while not tokens[0] == 'Aggregate':

        shell_name = tokens[0]
        shell_size = int(tokens[1])

        if shell_name not in shells_dict:
            shells_dict[shell_name] = []

        if shell_size not in shells_dict[shell_name]:
            shells_dict[shell_name].append(shell_size)

        tokens = input().split(' ')

    for key, value in shells_dict.items():
        avg_shell_size = math.ceil(sum(value) - (sum(value) / len(value)))
        print(f"{key} -> {', '.join(map(str, value))} ({avg_shell_size})")
