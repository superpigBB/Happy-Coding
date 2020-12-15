"""Given an list of integers, sort the elements in the list in ascending order. The quick sort algorithm should be
used to solve this problem.

Examples

{1} is sorted to {1}
{1, 2, 3} is sorted to {1, 2, 3}
{3, 2, 1} is sorted to {1, 2, 3}
{4, 2, -3, 6, 1} is sorted to {-3, 1, 2, 4, 6}
Corner Cases

What if the given list is null? In this case, we do not need to do anything.
What if the given list is of length zero? In this case, we do not need to do anything.
"""

class Solution(object):
    """
    解题思路：recursion: 选一个pivotal， 左边右边排序 => 参见Sort Integers II.py
    Time: O(nlogn)
    Space: O(logn)
    """

    def quickSort(self, list):
        """
        input: int[] list
        return: int[]
        """
        # corner cases
        if len(list) == 0 or len(list) == 1:
            return list

        ## quicksort divide and conquer
        self.quicksort(list, 0, len(list) - 1)
        return list

    def quicksort(self, list, start, end):
        # base cases
        if start >= end:
            return

        left, right = start, end

        # 可以取mid index value 或 pivot取随机数
        pivot = list[(left + right) / 2]
        # import random
        # pivot = list[left + int(random.random() * (right - left + 1))]

        while left <= right:
            while left <= right and list[left] < pivot:
                left += 1

            while left <= right and list[right] > pivot:
                right -= 1
            # 互换
            if left <= right:
                list[left], list[right] = list[right], list[left]
                right -= 1
                left += 1

        self.quicksort(list, start, right)
        self.quicksort(list, left, end)



print(Solution().quickSort([3,5,1,2,4,8]))    # 1 2 3 4 5 8