class Solution(object):
    def majorityElement(self, nums):
        
        dictionary = {}

        for number in nums:
            if number not in dictionary:
                dictionary[number] = 1
            else:
                dictionary[number] = dictionary[number] + 1
        
        half = len(nums)/2 

        for key in dictionary:

            if dictionary[key] > half:
                return key
        