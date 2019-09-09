def bubble_sort_algorithm(collection):
    length = len(collection)

    for i in range(length):
        swapped = False
        for j in range(0, length - 1 - i):
            if collection[j] > collection[j + 1]:
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
                swapped = True
        if not swapped:
            break


if __name__ == '__main__':
    nums = list(map(int, input().split(' ')))

    bubble_sort_algorithm(nums)

    print(' '.join(map(str, nums)))
