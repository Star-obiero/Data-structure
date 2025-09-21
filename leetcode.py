"""
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer
 range [-231, 231 - 1], then return 0.

"""

class Solution:
    def reverse(self, x):
        int_min,int_max=-2**31,2**31-1

        result= 0
        sign=-1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            digit = X % 10
            x //=10

            if result > (int_max-digit) // 10:
                return 0
            
            result=result * 10 + digit
        return sign * result
        