class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        result = 0
        sum = 0
        startWindow = 0

        for endWindow in range(len(arr)):
            # adds the last element on the window
            sum += arr[endWindow]
            # checks if the size of the window is size k
            if endWindow >= k - 1:
                if sum/k >= threshold:
                    result += 1
                # substract the first element in the window
                sum -= arr[startWindow]
                # shit the window to the next value
                startWindow += 1

        return result
