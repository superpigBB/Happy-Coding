"""
Given a target integer T and an integer array A sorted in ascending order,
Find the total number of occurrences of T in A.

Examples

A = {1, 2, 3, 4, 5}, T = 3, return 1
A = {1, 2, 2, 2, 3}, T = 2, return 3
A = {1, 2, 2, 2, 3}, T = 4, return 0
Corner Cases

What if A is null? We should return 0 in this case.
"""


class Solution(object):
    """
    解题思路：
    """
    def totalOccurrence(self, array, target):
        """
        input: int[] array, int target
        return: int
        """
        # write your solution here