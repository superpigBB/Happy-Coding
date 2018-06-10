# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output:  321
# Example 2:
#
# Input: -123
# Output: -321
# Example 3:
#
# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range.
# For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


### Original method
### transfer x into a string, use for loop to copy paste from end character to start character
### Time Complexity O(N), Space Complexity O(1)
### Takes 48s >64%
# class Solution(object):
#     def reverse(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#         ### exclude extreme values first
#         if x == 0:
#             return 0
#
#         if x < 0:   start, new_string = 0, '-'
#         elif x > 0: start, new_string = -1, ''
#
#         string_x = str(x)
#         for i in xrange(len(string_x) - 1, start, -1):
#             new_string = new_string + string_x[i]
#         if int(new_string)  < -2**31 or int(new_string)  > 2 **31 - 1:
#             return 0
#         else:
#             return int(new_string)
#


### Method 2: take advantage of string [first:end:add/minus by]
### O(1), O(1)
### not too much improvement 45s >74.5%
# class Solution(object):
#     def reverse(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#         ### exclude extreme values first
#         if x == 0:
#             return 0
#         if x > 0: new_string = str(x)[::-1]
#         elif x <0 : new_string = str(x)[::-1][-1] + str(x)[::-1][:-1]
#
#         if int(new_string) < -2 ** 31 or int(new_string) > 2 ** 31 - 1:
#             return 0
#         else:
#             return int(new_string)


# Method 3: use onlines solution: which directly transform reversed into integer by several mathematical calculation
### take advantage of cmp(a, b) to print final num -1 or 1
### O(n) and O(1)
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ### exclude extreme values first
        if x == 0:
            return 0
        num = abs(x)
        total = 0
        while (num > 0):
            digit = num % 10
            total += digit * 10 ** (len(str(num)) - 1)
            num   = num / 10
        if total > 2 ** 31:
            return 0
        else:
            return cmp(x, 0) * total



obj = Solution()
print obj.reverse(123)
print obj.reverse(-32456)
print obj.reverse(-2**32)
print obj.reverse(0)
