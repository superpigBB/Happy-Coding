# Given an integer n, return the number of trailing zeroes in n!.
#
# Note: Your solution should be in logarithmic time complexity.

### Solution 1: normal method: Time Limit Exceeded!!! need log(n)
### Time O(n) Space O(1)


import math

class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 1
        while n >= 1:
            result = result * n
            n -= 1

        trailing_cnt = 0
        while result % 10 == 0:
            trailing_cnt += 1
            result = result //10
        return trailing_cnt


# print(Solution().trailingZeroes(3)) #6  - 0
# print(Solution().trailingZeroes(5)) #120 -1


### Solution 2: 找规律，以5为目标
### Time O(logn) Space O(1)



class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        trailing_cnt = 0
        while n > 0:
            trailing_cnt += n // 5
            n = n //5

        return trailing_cnt


# print(Solution().trailingZeroes(3)) #6  - 0
# print(Solution().trailingZeroes(5)) #120 -1

### Solution 2.2 :递归
### Time O(logn) Space O(logn)



class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 0 if n == 0 else n//5 + self.trailingZeroes(n//5)


print(Solution().trailingZeroes(3)) #6  - 0
print(Solution().trailingZeroes(5)) #120 -1
