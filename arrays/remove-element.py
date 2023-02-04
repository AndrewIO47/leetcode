
def removeElement(self, nums, val):

    k = 0
    for i in range(len(nums)):
        curr = nums[i]

        if curr != val:
            nums[k] = curr
            k += 1
