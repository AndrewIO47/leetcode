# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # edge base
        if isBadVersion(n[0]):
            return 0

        good_version = 0

        while good_version <= n:

            mid = (good_version + n) // 2

            if isBadVersion(mid) == False:
                good_version = mid

            else:
                for i in range(good_version, mid):
                    if isBadVersion(i):
                        return i

                    good_version = i
