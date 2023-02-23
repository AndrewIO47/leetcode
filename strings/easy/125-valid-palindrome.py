import re


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # removes all the non-alphanumeric characters
        # and makes everything to lowercase
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        backwardString = ''

        for i in reversed(s):
            backwardString += i

        if s == backwardString:
            return True

        return False
