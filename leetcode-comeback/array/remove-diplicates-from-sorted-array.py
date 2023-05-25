class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        hashset = set() #creates a hashset
        
        for number in nums: 
            if number not in hashset: 
                hashset.add(number)
                nums[k] = number
                k += 1 

        return k
            