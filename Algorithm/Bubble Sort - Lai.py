"""
Bubble Sort
example: [4, 2, -3, 6, 1]
"""


class Solution(object):
    """
    解题思路： 冒泡排序就是从unsorted list里从一端开始俩俩比较，把大的那个往右移，直到换到最后一个，然后再重复之前的n-1排序
    Time: O(N^2)
    Space: O(1)
    """

    def solve(self, list):
        """
        input: int[] list
        return: int[]
        """
        # write your solution here
        """Corner Cases"""
        if list is None or len(list) == 0:
            return []

        for i in range(1, len(list) - 1):
            for j in range(len(list) - i):
                if list[j] > list[j + 1]:
                    list[j], list[j + 1] = list[j + 1], list[j]

        return list

    """wikipedia method"""
    def solve2(self, list):
        n = len(list)

        # Traverse through all array elements
        for i in range(n):
            # Last i elements are already in place
            for j in range(n - i - 1):
                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if list[j] > list[j + 1]:
                    list[j], list[j + 1] = list[j + 1], list[j]

        return list

print(Solution().solve([4, 2, -3, 6, 1]))

print(Solution().solve2([4, 2, -3, 6, 1]))