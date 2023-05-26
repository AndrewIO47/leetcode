import re


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Convert uppercase letters to lowercase
        converted_string = s.lower()

        # Remove non-alphanumeric characters using regular expressions
        converted_string = re.sub(r'[^a-zA-Z0-9]', '', converted_string)

        # reverse the string 
        
        # naive solution
        # backward_string = ""
        # for char in reversed(converted_string):
        #     backward_string += char
        
        # optimal solution 
        backward_string = converted_string[::-1]
        return converted_string == backward_string