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
        """corner cases"""
        if len(array) == 0 or array is None:
            return []

        for i in range(len(array)):
            min_index = i  # set smallest number at the first place of list
            for j in range(i + 1, len(array)):
                if array[j] < array[min_index]:
                    min_index = j

            if min_index == i:
                pass # if min index已经在unsorted list最左边，不用交换
            else:
                array[i], array[min_index] = array[min_index], array[i]

        return array


print(Solution().solve([3, 2, 1]))
print(Solution().solve([4, 2, -3, 6, 1]))