import numbers


def merge(nums1, m, nums2, n):

    #   last index in nums1
    setter = m + n - 1

#  merge backwards
    while m > 0 and n > 0:
        curr1 = nums1[m - 1]
        curr2 = nums2[n - 1]

        if (curr1 < curr2):
            nums1[setter] = curr2
            setter -= 1
        else:
            nums1[setter] = curr1
            setter -= 1

#  merge the remaining numbers in nums2
    while n > 0:
        nums1[setter] = nums2[n-1]
        n -= 1
        setter -= 1
