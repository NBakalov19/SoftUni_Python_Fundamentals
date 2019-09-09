nums = input().split(' ')

have_equal_neighbours = True

while have_equal_neighbours:
    for index in range(len(nums) - 1):
        if nums[index] == nums[index + 1]:
            new_element = nums[index] + nums[index + 1]
            nums.remove(nums[index])
            nums.remove(nums[index])
            nums.insert(index, new_element)
            break
        
        if index == len(nums) - 2:
            have_equal_neighbours = False

print(' '.join(map(str, nums)))
