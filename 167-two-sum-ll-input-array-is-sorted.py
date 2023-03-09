class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        right = len(numbers)-1
        left = 0

        while left < right:

            sum = numbers[left] + numbers[right]

            if sum > target:
                right -= 1
            elif sum < target:
                left += 1
            else:
                return [left+1, right+1]

        return
d