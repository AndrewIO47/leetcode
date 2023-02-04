from re import search


def searchInsert(nums, target):

    #   edge case were the target is in the first or last position of the list
    if target < nums[0]:
        return 0
    elif target > nums[len(nums)-1]:
        return len(nums)

#   search for the target position
    for i in range(len(nums)):
        curr_num = nums[i]

        if (curr_num == target):
            return i
        else:
            if target > curr_num and target < nums[i+1]:
                return i+1


nums = [2, 2, 4, 6]
target = 1
print(searchInsert(nums, target))
