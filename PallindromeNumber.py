# Given an integer x, return true if x is a 
# palindrome
# , and false otherwise.

 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # if x<0:
        #     return False
        # reversed_num = 0
        # temp = x

        # while(temp != 0):
        #     digit = temp % 10
        #     reversed_num = reversed_num * 10 + digit
        #     temp //= 10
        # return reversed_num == x

        if x<0 or (x!=0 and x%10==0):
            return False
        reversed_num = 0
        original = x
        while x>reversed_num:
            reversed_num = reversed_num*10 + x%10
            x //=10
        return x==reversed_num or x == reversed_num//10