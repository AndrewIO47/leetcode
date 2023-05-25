class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        digits.reverse()
        carry = 1 
        k = 0
        
        while carry == 1 and k < len(digits):
            
            current_digit = digits[k]
            
            if current_digit == 9:
                digits[k] = 0 
            else:
                digits[k] = current_digit + 1 
                carry = 0 
            
            k+=1
            
        if carry == 1: 
            digits.append(1)
        
        digits.reverse()
        return digits

        print (digits_reversed)