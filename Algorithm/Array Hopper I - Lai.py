"""
Given an array A of non-negative integers, you are initially positioned at index 0 of the array.
A[i] means the maximum jump distance from that position (you can only jump towards the end of the array).
Determine if you are able to reach the last index.

Assumptions

The given array is not null and has length of at least 1.
Examples

{1, 3, 2, 0, 3}, we are able to reach the end of array(jump to index 1 then reach the end of the array)

{2, 1, 1, 0, 2}, we are not able to reach the end of array
"""


class Solution(object):
    """"""
    """
    解题思路： greedy method: 对每个array的index位置进行记录长度，判断和array实际len比较
    Time： O(n)
    Space: O(1)
    """

    def canJump(self, array):
        """
        input: int[] array
        return: boolean
        """
        # write your solution here
        # corner cases
        if not array or len(array) <= 1:
            return True

        n, max_dist = len(array), 0

        for i in range(n):
            if max_dist >= i:
                max_dist = max(max_dist, i + array[i])
                if max_dist >= n - 1:
                    return True

        return False