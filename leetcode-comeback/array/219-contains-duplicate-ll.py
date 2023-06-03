class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dictionary = {}

        for i in range(len(nums)):
            
            cur_number = nums[i]

            if cur_number not in dictionary:
                dictionary[cur_number] = i 
            else:
                
                if abs(dictionary[cur_number] - i) <= k:
                    return True
                else: 
                    dictionary[cur_number] = i
        
        return False 
