class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        dictionary = {}

        for letter in s: 
            if letter not in dictionary:
                dictionary[letter] = 1
            else:
                dictionary[letter] = dictionary.get(letter) + 1

        
        for i in range(len(s)):
            letter = s[i]
            
            if dictionary[letter] == 1:
                return i
        
        return -1
