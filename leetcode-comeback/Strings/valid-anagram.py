class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dictionary_s = {}
        #adds all the letters along with its count
        for letter in s: 
            if letter not in dictionary_s:
                dictionary_s[letter] = 1
            else: 
                dictionary_s[letter] = dictionary_s[letter] + 1
        
        dictionary_t = {}
        #adds all the letters along with its count
        for letter in t: 

            if letter not in dictionary_t:
                dictionary_t[letter] = 1
            else: 
                dictionary_t[letter] = dictionary_t[letter] + 1
        
        # compare if they are equal 
        return dictionary_s == dictionary_t