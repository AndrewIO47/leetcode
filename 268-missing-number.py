def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # initialize result to the length of the array
    result = len(nums)

    for i in range(len(nums)):
        # by doing result += (i - nums[i]) we can find the missing number
        # becasue we know that the range goes from [o,n] and we are going to be
        # left with the missing number
        result = result + (i-nums[i])

    return result


# nums = [3, 0, 1]
# missingNumber(nums)
nums = [0, 1]
missingNumber(nums)

# nums = [8, 6, 4, 2, 3, 5, 7, 0, 1]
# missingNumber(nums)
