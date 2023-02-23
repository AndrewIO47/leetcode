class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        hashmapS = {}
        hashmapT = {}

        # add each letter to the hashmap and increase the times it appears
        for i in s:
            if i not in hashmapS:
                hashmapS[i] = 1
            else:
                hashmapS[i] = hashmapS[i] + 1

        for i in t:
            if i not in hashmapT:
                hashmapT[i] = 1
            else:
                hashmapT[i] = hashmapT[i] + 1

        # compare if they have the same elements
        if hashmapS == hashmapT:
            return True

        return False
