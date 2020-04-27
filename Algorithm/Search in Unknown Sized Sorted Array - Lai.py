"""
Given a integer dictionary A of unknown size, where the numbers in the dictionary are sorted in ascending order,
determine if a given target integer T is in the dictionary. Return the index of T in A, return -1 if T is not in A.

Assumptions

dictionary A is not null
dictionary.get(i) will return null(Java)/INT_MIN(C++)/None(Python) if index i is out of bounds
Examples

A = {1, 2, 5, 9, ......}, T = 5, return 2
A = {1, 2, 5, 9, 12, ......}, T = 7, return -1
"""


# Definition for a unknown sized dictionary.
# class Dictionary(object):
#   def get(self, index):
#     pass

class Solution(object):
    """
    解题思路：虽然从list变成了dict, 但仍然是一道类似sorted list, 而且找target的题，所以用binary search;
    但因为Unknown size, end无法得知， 所以无法求得mid所在位置；
    按九章以前教法，我记得是倍数增加寻找边界值end，然后再用二分法
    Time: O(k + log(k))  => k is the first index where element value > target
    Space: O(1)
    """

    def search(self, dic, target):
        """
        input: Dictionary dic, int target
        return: int
        """
        # write your solution here
        """ Corner Cases """
        if dic.get(0) is not None and dic.get(0) > target:
            return -1

        # 先找到end边界值： 利用快速2倍查找
        start, end = 0, 1
        while dic.get(end) is not None and dic.get(end) < target:
            # recursively reduce intervals between start and end until element of end index >= target
            start = end
            end = end * 2

        if dic.get(end) == target:
            return end
        else:
            return self.binary_search(dic, start, end, target)

    def binary_search(self, new_dic, start, end, target):
        while start <= end:
            mid = (start + end) // 2
            if new_dic.get(mid) and new_dic.get(mid) == target:
                return mid
            elif new_dic.get(mid) and new_dic.get(mid) > target:
                end = mid - 1
            else:
                start = mid + 1

        return -1
