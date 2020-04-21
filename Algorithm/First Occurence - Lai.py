"""
Given a target integer T and an integer array A sorted in ascending order,
find the index of the first occurrence of T in A or return -1 if there is no such index.

Assumptions

There can be duplicate elements in the array.
Examples

A = {1, 2, 3}, T = 2, return 1
A = {1, 2, 3}, T = 4, return -1
A = {1, 2, 2, 2, 3}, T = 2, return 1
Corner Cases

What if A is null or A of zero length? We should return -1 in this case.
"""


class Solution(object):
    """
    解题思路： 第一次出现，则必须保证左边界完全被保留，所以如果找到，让右边界指向那个index，以防漏了左边界
    和binary search一样的时间复杂度和空间复杂度
    Time: O(log(n))
    Space: O(1)
    """
    def firstOccur(self, list, target):
        """
        input: int[] list, int target
        return: int
        """
        # write your solution here
        """corner cases"""
        if len(list) == 0 or list is None or len(list) == 1 and target not in list:
            return -1

        start, end = 0, len(list) - 1
        while start < end - 1:
            mid = (start + end) // 2
            if list[mid] == target:
                end = mid
            elif list[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        if list[start] == target:
            return start
        elif list[end] == target:
            return end
        else:
            return -1


print(Solution().firstOccur([1, 2, 3], 2))  # 1
print(Solution().firstOccur([1, 2, 3], 4))  # -1
print(Solution().firstOccur([1, 2, 2, 2, 3], 2))  # 1
print(Solution().firstOccur([1], 5))  # -1

