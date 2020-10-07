"""
Find the K smallest numbers in an unsorted integer list A. The returned numbers should be in ascending order.

Assumptions

A is not null
K is >= 0 and smaller than or equal to size of A
Return

an list with size K containing the K smallest numbers in ascending order
Examples

A = {3, 4, 1, 2, 5}, K = 3, the 3 smallest numbers are {1, 2, 3}
"""

"""
---------------------TO DO -------------------
解题思路：两种方法 
方法 1.quick select (reference 九章 Kth Largest Element in an list.py AND LaiOffer课) 
       Time: O(n + klogk) Space: O(k) 
       => TO DO: Better to follow up Laioffer's! Much more pro!!!
方法 2.max heap   => TO DO !!!    
"""


class Solution(object):

    """
    方法 2. quick select
    Time:
    """


    """
    方法 1. quick select
    Time: O(n + klogk)
    Space: O(k)
    """
    def kSmallest(self, list, k):

        """
        input: int[] list, int k
        return: int[]
        """
        # write your solution here

        """Corner Cases"""
        if list is None or k > len(list) or k == 0:
            return []

        """
        quickSelect to find kth smallest element; after that, the first k elements in the array are the k smallest
        but not sorted
        """
        self.quickSelect(list, k - 1, 0, len(list) - 1)
        result_list = list[:k]
        result_list.sort()
        return result_list

    """Quick Select Function"""
    def quickSelect(self, list, target_index, start, end):
        # define two moving pointers
        left, right = start, end
        # take middle index of list as pivot value
        mid = (start + end) // 2
        pivot_value = list[mid]

        # similar quickSort template for sorting left and right
        while left <= right:
            while left <= right and list[left] < pivot_value:
                left += 1

            while left <= right and list[right] > pivot_value:
                right -= 1

            if left <= right:
                list[left], list[right] = list[right], list[left]
                left += 1
                right -= 1

        """
           unlike quick sort, we only need to do quickselect on at most one partion 
           if the pivot is already the kth smallest element, we can directly return
           if the pivot is already the kth smallest element, we can directly return
        """
        if target_index == right:
            return
        elif target_index < right:   # only need to recursively call quick select on the left partition
            self.quickSelect(list, target_index, start, right)
        else:    # only need to recursively call quick select on the right partition
            self.quickSelect(list, target_index, left, end)



print(Solution().kSmallest([3, 1, 5, 2, 4], 4))    # [1, 2, 3, 4]
print(Solution().kSmallest([3, 4, 1, 2, 5], 3))    # [1, 2, 3]
print(Solution().kSmallest([3, 1, 5, 2, 4], 2))    # [1, 2]
