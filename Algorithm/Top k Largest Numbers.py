"""
Given an integer array, find the top k largest numbers in it.

Example
Example1

Input: [3, 10, 1000, -99, 4, 100] and k = 3
Output: [1000, 100, 10]
Example2

Input: [8, 7, 6, 5, 4, 3, 2, 1] and k = 5
Output: [8, 7, 6, 5, 4]
"""


class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """

    """
    方法一： 用quicksort =>晚点再写
    """

    """
    方法二：直接sort，但应该不行
    Time: O(nlogk), Space: O(1)
    """

    def topk(self, nums, k):
        # write your code here
        import heapq
        heapq.heapify(nums)
        return heapq.nlargest(k, nums)
