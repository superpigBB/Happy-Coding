"""Given a target integer T and an integer array A sorted in ascending order, find the index i such that A[i] == T
or return -1 if there is no such index.

Assumptions

There can be duplicate elements in the array, and you can return any of the indices i such that A[i] == T.
Examples

A = {1, 2, 3, 4, 5}, T = 3, return 2
A = {1, 2, 3, 4, 5}, T = 6, return -1
A = {1, 2, 2, 2, 3, 4}, T = 2, return 1 or 2 or 3
Corner Cases

What if A is null or A is of zero length? We should return -1 in this case.
"""


class Solution(object):
    """
    解题思路： 一般用二分法是base on sorted list 然后对分找target value
    Time: O(logn)
    Space: O(1)
    """
    def binarySearch(self, list, target):
        """
        input: int[] list, int target
        return: int
        """
        # write your solution here
        """Corner Cases： 问面试官应该return多少"""
        if list is None or len(list) == 0 or len(list) == 1 and target not in list:
            return -1

        start = 0; end = len(list) - 1
        # 跳出条件： start > end
        while start <= end:
            mid = (start + end) // 2

            # mid value vs. target
            if list[mid] == target:
                return mid
            elif list[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return -1



print(Solution().binarySearch([1, 2, 3, 4, 5], 3))  # 2
print(Solution().binarySearch([1, 2, 3, 4, 5], 6))  # -1
print(Solution().binarySearch([1, 2, 2, 2, 3, 4], 2))  # 2 or 3

