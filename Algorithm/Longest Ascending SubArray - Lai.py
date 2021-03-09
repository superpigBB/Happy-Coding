"""
Given an unsorted array, find the length of the longest subarray in which the numbers are in ascending order.

Assumptions

The given array is not null
Examples

{7, 2, 3, 1, 5, 8, 9, 6}, longest ascending subarray is {1, 5, 8, 9}, length is 4.

{1, 2, 3, 3, 4, 4, 5}, longest ascending subarray is {1, 2, 3}, length is 3.

"""


class Solution(object):
    """"""
    """
    解题思路：因为是求最值，而且发现数据之间有重叠关系，最优解应该是DP
    设置global max然后追踪第i - 1的值然后和当前i的值比较，来确定ascending cnt,
    然后和global max比较计算global max
    Time: O(n)
    Space: O(1)
    """

    def longest(self, array):
        """
        input: int[] array
        return: int
        """
        # write your solution here
        # corner casese
        if array is None or len(array) == 0:
            return 0
        if len(array) == 1:
            return 1

        global_max = float('-inf')
        asc_cnt = 1

        for i in range(1, len(array)):
            if array[i] - array[i - 1] > 0:
                asc_cnt += 1
            else:
                asc_cnt = 1
            global_max = max(global_max, asc_cnt)

        return global_max
