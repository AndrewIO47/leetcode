class Solution(object):
    # Naive approach 
    # def twoSum(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: List[int]
    #     """
        
    #     for i in range(len(nums)):

    #         for j in range(i+1 , len(nums)):
    #             sum = nums[i] + nums[j]

    #             if sum == target:
    #                 return [i,j]
            

    # Optimal 
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
    
        k = 0 
        dictionary = {}

        for number in nums:

            newTarget = target - number

            if newTarget not in dictionary:
                dictionary[number] = k
            else:
                value = dictionary.get(newTarget) 
                return [value,k]
            
            k+=1