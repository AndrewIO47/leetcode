class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        front = 0 
        back = len(nums)-1
        counter = 0 
        
        # sorts the array and puts number in place 
        for number in nums:
            if number != 0:
                nums[front] = number 
                front += 1
            else:
                counter += 1
        
        # add the zeros to the end of the array
        for i in range(counter):
            nums[back] = 0
            back -= 1

        return nums