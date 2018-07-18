# Description
# Find any position of a target number in a sorted array. Return -1 if target does not exist.
#
# Example
# Given [1, 2, 2, 4, 5, 5].
#
# For target = 2, return 1 or 2.
#
# For target = 5, return 4 or 5.
#
# For target = 6, return -1.
#
# Challenge
# O(logn) time

class Solution:
    """
    @param: nums: An integer array sorted in ascending order
    @param: target: An integer
    @return: An integer
    """

    ## sorted array 的话可以用O（N）时间复杂度直接扫一遍然后返回position
    ## 但challenge 在于O(logn)的时间复杂度，一般logn首先想到的是binary search
    ## 这题的话就用binary search先找到中点的值，然后和target作对比，扔掉一边做search
    ## Time: O(logn), Space: O(1)
    def findPosition(self, nums, target):
        # write your code here
        ## corner cases
        if nums is None or len(nums) == 0:
            return -1

        start = 0
        end = len(nums) - 1

        while start + 1 < end:  # to avoid endless loop
            mid = start + (end - start) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                start = mid + 1  ## or directly use start = mid

            elif nums[mid] > target:
                end = mid - 1  ## or directly use end = mid

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end

        return -1