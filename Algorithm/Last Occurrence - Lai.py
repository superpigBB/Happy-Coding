"""
Given a target integer T and an integer array A sorted in ascending order,
find the index of the last occurrence of T in A or return -1 if there is no such index.

Assumptions

There can be duplicate elements in the array.

Examples

A = {1, 2, 3}, T = 2, return 1
A = {1, 2, 3}, T = 4, return -1
A = {1, 2, 2, 2, 3}, T = 2, return 3
Corner Cases

What if A is null or A is array of zero length? We should return -1 in this case.
"""


class Solution(object):
    """
    解题思路： 和first occurence 类似， 但现在是找last， 相当于保留左边界，因为不确定左边界是不是最后一个
    还是similar to binary search
    Time: O(logn)
    Space: O(1)
    """
    def lastOccur(self, array, target):
        """
        input: int[] list, int target
        return: int
        """
        # write your solution here
        """Corner Cases: better to ask interviewer to confirm the return value of corner cases"""
        if len(list) == 0 or list is None or len(list) == 1 and target not in list:
            return -1

        start, end = 0, len(list) - 1
        while start < end - 1:
            mid = (start + end) // 2
            if list[mid] == target:
                start = mid
            elif list[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        if list[end] == target:
            return end
        elif list[start] == target:
            return start

        return -1

print(Solution().lastOccur([1, 2, 3], 2))  # 1
print(Solution().lastOccur([1, 2, 3], 4))  # -1
print(Solution().lastOccur([1, 2, 2, 2, 3], 2))  # 3
print(Solution().lastOccur([1], 2))  # -1



