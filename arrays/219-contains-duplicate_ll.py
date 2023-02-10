def containsNearbyDuplicate(nums, k):

    hashmap = {}

    for i in range(len(nums)):
        cur_number = nums[i]
        if cur_number in hashmap and abs(hashmap[cur_number] - i) <= k:
            print("current: " + str(cur_number))
            print("i " + str(i))
            print("k: " + str(k))
            print("hashmap[cur_number]: " + str(hashmap[cur_number]))
            return True
        else:
            hashmap[cur_number] = i

    return False


nums = [1, 2, 3, 1, 2, 3]
k = 2
print(containsNearbyDuplicate(nums, k))
