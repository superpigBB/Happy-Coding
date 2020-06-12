"""
Find the K smallest numbers in an unsorted integer array A. The returned numbers should be in ascending order.

Assumptions

A is not null
K is >= 0 and smaller than or equal to size of A
Return

an array with size K containing the K smallest numbers in ascending order
Examples

A = {3, 4, 1, 2, 5}, K = 3, the 3 smallest numbers are {1, 2, 3}
"""

"""
解题思路：两种方法 
方法 1.quick select (九章 Kth Largest Element in an Array.py) 
                Time: O(1) Space: O(1)
方法 2.             
"""
class Solution(object):

  def kSmallest(self, array, k):
    """
    input: int[] array, int k
    return: int[]
    """
    # write your solution here
