"""
K Closest In Sorted list
Medium
Given a target integer T, a non-negative integer K and an integer list A sorted in ascending order,
find the K closest numbers to T in A. If there is a tie, the smaller elements are always preferred.

Assumptions

A is not null
K is guranteed to be >= 0 and K is guranteed to be <= A.length
Return

A size K integer list containing the K closest numbers(not indices) in A,
sorted in ascending order by the difference between the number and T.
Examples

A = {1, 2, 3}, T = 2, K = 3, return {2, 1, 3} or {2, 3, 1}
A = {1, 4, 6, 8}, T = 3, K = 3, return {4, 1, 6}
"""


class Solution(object):
    """
    解题思路：有target value, and list is a sorted list => binary search基本直接能判定
    实际这题有点像find closest element的进阶，相当于先用binary search找到那个closest element in list;
    然后再在那个数的list的位置附近找K个数
    Time：O(logn + k) => O(logn)
    Space: O(k)
    """
    """2nd 参考其他optimized解法写的 TODO """
    def kClosest1(self, list, target, k):
        """
        input: int[] list, int target, int k
        return: int[]
        """
        # write your solution here

    


    """1st 自己第一次写的"""
    def kClosest1(self, list, target, k):
        """
        input: int[] list, int target, int k
        return: int[]
        """
        # write your solution here
        """Corner Cases: better ask interviewer to confirm return value for corner cases"""
        if list is None or len(list) == 0 or k == 0:
            return []


        """find closest element from target first in list"""
        start, end = 0, len(list) - 1
        closest_index = None  # temp val for closest index
        while start < end - 1:
            mid = (start + end) // 2
            if list[mid] == target:
                closest_index = mid
                break
            elif list[mid] > target:
                end = mid
            else:
                start = mid

        # locate closest index
        if closest_index is None:   # if closest_index not defined
            closest_index = start if abs(list[start] - target) <= abs(list[end] - target) else end

        """make that closet element a centered value and set two pointers i & j to get the k closest"""
        i, j = closest_index - 1, closest_index + 1
        return_list = [list[closest_index]]  # return list to store sorted elemets according to |e.value - target|
        if len(return_list) == k:     # if k == 1
            return return_list

        while i >= 0 and j <= len(list) - 1:
            if abs(list[i] - target) <= abs(list[j] - target):
                return_list.append(list[i])
                i -= 1
            else:
                return_list.append(list[j])
                j += 1

            if len(return_list) == k:
                return return_list

        if i < 0:
            return_list.extend(list[j:(j + k - len(return_list))])
            return return_list
        if j > len(list) - 1:
            if i - (k - len(return_list)) < 0:
                return_list.extend(list[i::-1])
            else:
                return_list.extend(list[i : i - (k - len(return_list)): -1])
            return return_list

print(Solution().kClosest([1, 2, 3], target=2, k=1))  # [2]
# print(Solution().kClosest([1, 2, 3], target=2, k=3))  # [2, 1, 3] or [2, 3, 1]
# print(Solution().kClosest([1, 4, 6, 8], target=3, k=3))  # [4, 1, 6]
# print(Solution().kClosest([1, 2, 4, 6, 7, 8, 9], target=7.5, k=5))  # [7, 8, 6, 9, 4]
# print(Solution().kClosest([1, 2, 4, 6, 7, 8, 9], target=0, k=3))  # [1, 2, 4]
# print(Solution().kClosest([1, 2, 4, 6, 7, 8, 9], target=9, k=1))  # [9]
# print(Solution().kClosest([1, 3, 5], target=10, k=3))  # [5， 3，1]
# print(Solution().kClosest([1], target=0, k=0))  # []
