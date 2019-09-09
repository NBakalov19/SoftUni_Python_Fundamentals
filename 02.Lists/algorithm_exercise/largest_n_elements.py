def insertion_sort(collection):
    for i in range(1, len(collection)):
        key = collection[i]

        j = i - 1

        while j >= 0 and key < collection[j]:
            collection[j + 1] = collection[j]
            j = j - 1

        collection[j + 1] = key


if __name__ == '__main__':
    nums = list(map(int, input().split(' ')))
    count_elements = int(input())

    insertion_sort(nums)
    nums.reverse()

    print(' '.join(map(str, nums[0: count_elements])))
