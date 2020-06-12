"""
Find all numbers that appear in both of the two unsorted arrays, return the common numbers in increasing order.

Assumptions

Both arrays are not null.
There are no duplicate numbers in each of the two arrays respectively.
Exmaples

A = {1, 2, 3}, B = {3, 1, 4}, return [1, 3]
A = {}, B = {3, 1, 4}, return []
"""


class Solution(object):
    """
    Time: Onlogn(max(len(a), len(b)))
    Space: O(max(len(a), len(b)))
    """

    def common(self, a, b):
        """
        input: int[] a, int[] b
        return: Integer[]
        """
        # write your solution here
        """corner cases"""
        if (a is None or len(a) == 0) or (b is None or len(b) == 0):
            return []

        s = set(a)

        return sorted(x for x in b if x in s)