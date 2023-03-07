from turtle import right


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # initialize at the first value bc we have to take into consideration if nums are negative
        maxSum = nums[0]
        curSum = 0

        for i in nums:
            if curSum < 0:
                curSum = 0

            curSum = curSum + i
            maxSum = max(maxSum, curSum)

        return maxSum
