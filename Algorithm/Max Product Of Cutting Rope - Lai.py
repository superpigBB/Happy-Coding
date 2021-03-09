"""
Given a rope with positive integer-length n, how to cut the rope into m integer-length parts with length
p[0], p[1], ...,p[m-1], in order to get the maximal product of p[0]*p[1]* ... *p[m-1]? m is determined by you and must
be greater than 0 (at least one cut must be made). Return the max product you can have.

Assumptions

n >= 2
Examples

n = 12, the max product is 3 * 3 * 3 * 3 = 81(cut the rope into 4 pieces with length of each is 3).
"""


class Solution(object):
    """"""
    """
    解题思路： 因为是求最值，然后能通过穷举找到规律并可能有交叠计算的，所以用DP
    这里用左大段 + 右小段（就是右边不会被再分割的最小单位）思想
    Time: O(n^2)
    Space: O(n)
    """

    def maxProduct(self, length):
        """
        input: int length
        return: int
        """
        # write your solution here
        # corner cases
        if length in (0, 1):
            return 0
        if length == 2:
            return 1

        # init list to store values from bottom to top
        mem = [0] * (length + 1)
        mem[2] = 1

        for i in range(3, length + 1):
            for j in range(1, i):
                mem[i] = max(mem[i], max(mem[j], j) * (i - j))

        return mem[length]

