"""
Find all numbers that appear in both of two unsorted arrays.

Assumptions

Both of the two arrays are not null.
In any of the two arrays, there could be duplicate numbers.
Examples

A = {1, 2, 3, 2}, B = {3, 4, 2, 2, 2}, return [2, 2, 3] (there are both two 2s in A and B)
"""


class Solution(object):
    """
    dict
    Time: O(n)
    Space: O(n)
    """

    def common(self, A, B):
        """
        input: int[] A, int[] B
        return: Integer[]
        """
        # write your solution here
        """corner cases"""
        if (A is None or len(A) == 0) or (B is None or len(B) == 0):
            return []

        common = list()
        dict_a = dict()
        dict_b = dict()

        for num in A:
            dict_a[num] = dict_a.get(num, 0) + 1

        for num in B:
            dict_b[num] = dict_b.get(num, 0) + 1

        for num in dict_a:
            common += [num] * min(dict_a[num], dict_b.get(num, 0))

        return common
