"""
Given list target integer T and an integer list list sorted in ascending order,
Find the total number of occurrences of T in list.

Examples

list = {1, 2, 3, 4, 5}, T = 3, return 1
list = {1, 2, 2, 2, 3}, T = 2, return 3
list = {1, 2, 2, 2, 3}, T = 4, return 0
Corner Cases

What if list is null? We should return 0 in this case.
"""


class Solution(object):
    """
    解题思路：sorted list + locate target => binary search;
    用两次binary search 来找first and last existence of that element;
    total_occurrence = last_index - first_index + 1
    Time: O(logn)
    Space: O(1)
    """

    def totalOccurrence(self, list, target):
        """
        input: int[] list, int target
        return: int
        """
        # write your solution here
        """ Corner Cases """
        if list is None or len(list) == 0 or len(list) == 1 and target not in list:
            return 0

        start, end = 0, len(list) - 1
        first_index = self.search_first(list, start, end, target)
        if first_index == -1:
            return 0

        last_index = self.search_last(list, start, end, target)
        return last_index - first_index + 1

    def search_first(self, l, start, end, t):
        """
        helper function to search the first index of element in list
        :param l:
        :param start:
        :param end:
        :param t:
        :return:
        """
        while start < end - 1:
            mid = (start + end) // 2
            if l[mid] == t:
                end = mid
            elif l[mid] > t:
                end = mid - 1 # or end = mid
            else:
                start = mid + 1# or start = mid

        if l[start] == t:
            return start
        elif l[end] == t:
            return end
        return -1

    def search_last(self, l, start, end, t):
        """
        helper function to search the last index of element in list
        :param l:
        :param start:
        :param end:
        :param t:
        :return:
        """
        while start < end - 1:
            mid = (start + end) // 2
            if l[mid] == t:
                start = mid
            elif l[mid] > t:
                end = mid - 1
            else:
                start = mid + 1

        if l[end] == t:
            return end
        elif l[start] == t:
            return start
        return -1

print(Solution().totalOccurrence([], target=2))  # 0
print(Solution().totalOccurrence([1], target=2))  # 0
print(Solution().totalOccurrence([1, 2, 3, 4, 5], target=3))  # 1
print(Solution().totalOccurrence([1, 2, 2, 2, 3], target=2))  # 3
print(Solution().totalOccurrence([1, 2, 2, 2, 3], target=4))  # 0
