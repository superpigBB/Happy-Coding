# Description
# Find the last position of a target number in a sorted array. Return -1 if target does not exist.
#

# Example
# Given [1, 2, 2, 4, 5, 5].
#
# For target = 2, return 2.
#
# For target = 5, return 5.
#
# For target = 6, return -1.

class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """

    ## similar to First Position of Target
    def lastPosition(self, nums, target):
        # write your code here
        ## corner cases
        if nums is None or len(nums) == 0:
            return -1

        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                start = mid
            elif nums[mid] > target:
                end = mid - 1  ## or end = mid
            elif nums[mid] < target:
                start = mid + 1  ## or start = mid

        if nums[end] == target:
            return end
        if nums[start] == target:
            return start

        return -1
