"""
Given an list of integers, sort the elements in the list in ascending order.
The merge sort algorithm should be used to solve this problem.

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
    解题思路：recursion 数学归纳法 => 参见Sort Integers II.py
    Time： O（nlogn）
    Space: O(n)
    """
    def mergeSort(self, list):
        """
        input: int[] list
        return: int[]
        """
        # write your solution here
        """corner cases"""
        if list is None or len(list) == 0 or len(list) == 1:
            return list

        newlist = [0] * len(list)
        self.mergesort(list, 0, len(list) - 1, newlist)
        return list

    def mergesort(self, list, start, end, newlist):
        if start >= end:
            return

        mid = (start + end) // 2

        self.mergesort(list, start, mid, newlist)
        self.mergesort(list, mid + 1, end, newlist)

        self.merge(list, start, mid, end, newlist)

    def merge(self, list, start, mid, end, newlist):
        left = start
        right = mid + 1
        index = start

        while left <= mid and right <= end:
            if list[left] <= list[right]:
                newlist[index] = list[left]
                left += 1
            else:
                newlist[index] = list[right]
                right += 1

            index += 1

        while left <= mid:
            newlist[index] = list[left]
            left += 1
            index += 1

        while right <= end:
            newlist[index] = list[right]
            index += 1
            right += 1

        for index in range(start, end + 1):
            list[index] = newlist[index]

# print(Solution().mergeSort([1]))    # 1
print(Solution().mergeSort([3, 2, 1]))    # [1, 2, 3]
# print(Solution().mergeSort([4, 2, -3, 6, 1]))    # [-3, 1, 2, 4, 6]
