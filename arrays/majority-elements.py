def majorityElement(nums):

    hashmap = {}

    for key in nums:

        if key in hashmap:
            hashmap[key] = hashmap[key] + 1
        else:
            hashmap[key] = 1

    mayority = len(nums)/2

    for item in hashmap:
        if hashmap[item] > mayority:
            return item


majorityElement([2, 2, 1, 1, 1, 2, 2])
