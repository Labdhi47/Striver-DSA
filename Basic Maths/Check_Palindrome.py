# Check Palindrome 
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse_integer=0
        num=x
        while(x>0):
            last_digit=x%10
            reverse_integer=(reverse_integer*10)+last_digit
            x=x//10
        if reverse_integer==num:
            return True
        else:
            return False 
