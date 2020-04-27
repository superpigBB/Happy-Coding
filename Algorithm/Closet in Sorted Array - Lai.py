"""
Given a target integer T and an integer list A sorted in ascending order,
find the index i in A such that A[i] is closest to T.

Assumptions

There can be duplicate elements in the list, and we can return any of the indices with same value.
Examples

A = {1, 2, 3}, T = 2, return 1
A = {1, 4, 6}, T = 3, return 1
A = {1, 4, 6}, T = 5, return 1 or 2
A = {1, 3, 3, 4}, T = 2, return 0 or 1 or 2
Corner Cases

What if A is null or A is of zero length? We should return -1 in this case.
"""

class Solution(object):
    """
    解题思路：因为是sorted list, 而且又是给target找index的题，所以用binary search;
    基本上就是对半找value并依次进行缩小距离，如果一直找不到就缩小范围直到返回start and end指针；
    看start和end谁的absolute value更靠近A[i]即可
    Time: O(logn)
    Space: O(1)
    """
    def closest(self, list, target):
        """
        input: int[] list, int target
        return: int
        """
        # write your solution here
        """Corner Cases"""
        if list is None or len(list) == 0:
            return -1

        start, end = 0, len(list) - 1
        while start < end - 1:
            mid = (start + end) // 2
            if list[mid] == target:
                return mid       
            elif list[mid] > target:
                end = mid        # start/end都用mid是为了防止有遗漏cases
            else:
                start = mid

        return start if abs(list[start] - target) <= abs(list[end] - target) else end


print(Solution().closest([1, 2, 3], 2))    # 1
print(Solution().closest([1, 4, 6], 3))    # 1
print(Solution().closest([1, 4, 6], 5))    # 1 or 2
print(Solution().closest([1, 3, 3, 4], 2))  # 0 or 1 or 2
print(Solution().closest([1, 2, 6, 8], 3))  # 1





