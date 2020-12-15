"""
Given an array of integers, sort the elements in the array in ascending order. The selection sort algorithm should be used to solve this problem.

Examples

{1} is sorted to {1}
{1, 2, 3} is sorted to {1, 2, 3}
{3, 2, 1} is sorted to {1, 2, 3}
{4, 2, -3, 6, 1} is sorted to {-3, 1, 2, 4, 6}
Corner Cases

What if the given array is null? In this case, we do not need to do anything.
What if the given array is of length zero? In this case, we do not need to do anything.
"""

class Solution(object):
    """
    解题思路： 选择排序就是从unsorted list里面找最小的，放到第一位；然后继续找最小的在剩余的unsorted list里
    Time: O(N^2)
    Space: O(1)
    """
    def solve(self, array):
        """
        input: int[] array
        return: int[]
        """
        # write your solution here
        # corner cases
        if array is None or len(array) == 0 or len(array) == 1:
            return array

        for i in range(len(array) - 1):
            global_min = i
            for j in range(i + 1, len(array)):
                if array[j] < array[global_min]:
                    global_min = j
            if global_min != i:
                array[i], array[global_min] = array[global_min], array[i]

        return array


print(Solution().solve([3, 2, 1]))
print(Solution().solve([4, 2, -3, 6, 1]))