class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        result = ""
        carry = 0
        # reverse a and b so it is easier to work with it
        a = a[::-1]
        b = b[::-1]

        for i in range(max(len(a), len(b))):
            # edge case where a or b is > the other.
            if i < len(a):
                digitA = a[i]
            else:
                digitA = 0
            if i < len(b):
                digitB = b[i]
            else:
                digitB = 0
            sum = int(digitA) + int(digitB) + carry
            # reset the carry after adding it to the sum
            carry = 0
            # binary
            if sum == 0:
                result = "0" + result
            elif sum == 1:
                result = "1" + result
            elif sum == 2:
                result = "0" + result
                carry = 1
            elif sum == 3:
                result = "1" + result
                carry = 1

        # Edge case where the last sum left a carry
        if carry:
            result = "1" + result

        return result
