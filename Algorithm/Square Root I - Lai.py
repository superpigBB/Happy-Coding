"""
Given an integer number n, find its integer square root.

Assumption:

n is guaranteed to be >= 0.
Example:

Input: 18, Return: 4

Input: 4, Return: 2


"""

import math

class Solution(object):
    """
    解题思路：类似于在0, 1, 2, 3, 4, 5, 6, ... 的平方里，x离哪个e^2最近并且x >= e^2 ；
    实际就对等于在sorted list里面找一个最近的element^2 >= target <=>选最closest element and element^2 <= target
    Time: O(logn)
    Space: O(1)
    """
    """
     Optimized method by others 
     和我自己的方法一样，只是把mid * mid = x 改成 mid = x // mid, 为了避免乘方造成的overflow 
    """
    def sqrt(self, x):
        """
        input: int x
        return: int
        """
        # write your solution here
        """Corner Cases"""
        if x == 0 or x == 1:
            return x

        # find closest element whose **2 <=x
        start, end = 1, math.ceil(x / 2)   # start不能initialized to 0，怕divide error: 分母不能为0
        while start < end - 1:
            mid = (start + end) // 2  # or mid = start + (end - start) // 2
            if mid == x // mid:   # 用除法而不是用平方防止overflow
                return mid
            elif mid > x // mid:
                end = mid
            else:
                start = mid

        if start == x // start or end > x // end:
            return start
        if end <= x // end:
            return end


    """自己写的，但我觉得不够优化，可能存在overflow情况当数字一大"""

    def sqrt2(self, x):
        """
        input: int x
        return: int
        """
        # write your solution here
        # corner cases
        if x == 0 or x == 1:
            return x

        n = x // 2
        start, end = 1, n

        while start < end - 1:
            mid = (start + end) // 2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 < x:
                start = mid
            else:  # mid ** 2 > x
                end = mid - 1

        if end ** 2 > x:
            return start

        return end


print(Solution().sqrt(2))  # 1
print(Solution().sqrt(20))  # 4
print(Solution().sqrt(1))  # 1
print(Solution().sqrt(4))  # 2
print(Solution().sqrt(0))  # 0
print(Solution().sqrt(18))  # 4
