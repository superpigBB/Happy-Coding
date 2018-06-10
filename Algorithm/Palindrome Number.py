# Determine whether an integer is a palindrome. Do this without extra space.

### Original method: convert int x to string, check it's reversed value
### But the problem states "do this without extra space"! => better to use another way to directly process integers

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return  False
        return str(x) == str(x)[::-1]


### Second Solution: since if we directly reverse the integer, it might cause reveresed integer overflow,
### that's why we need to reverse only the half of integers: eg. 24142, 24 == 24
### Speed is almost the same but save more space!
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reverse, divided = 0, 0
        while x > reverse:
            divided = x % 10
            x = x // 10
            reverse = reverse * 10 + divided
        print(reverse, x)
        return reverse == x or x == reverse // 10






obj = Solution()
print (obj.isPalindrome(24))
print (obj.isPalindrome(22))
print (obj.isPalindrome(0))
print (obj.isPalindrome(24123))
print (obj.isPalindrome(24142))
print (obj.isPalindrome(-24142))
print (obj.isPalindrome(1))

