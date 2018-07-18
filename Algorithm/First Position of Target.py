# Description
# For a given sorted array (ascending order) and a target number, find the first index of this number in O(log n) time complexity.
#
# If the target number does not exist in the array, return -1.
#
#
# Example
# If the array is [1, 2, 3, 3, 4, 5, 10], for given target 3, return 2.
#
# Challenge
# If the count of numbers is bigger than 2^32, can your code work properly

class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """

    ## 因为是sorted array, 可以用O（N）走一遍并返回，但如果要求O(logn)， 那就要用二分法
    ## Time: O(logn), Space: O(1)
    def binarySearch(self, nums, target):
        # write your code here
        if nums is None or len(nums) == 0:
            return -1

        start = 0
        end = len(nums) - 1

        ## avoid infinite loop
        while start + 1 < end:
            mid = start + (end - start) // 2  ## avoid integer overflow
            if nums[mid] == target:
                end = mid
            elif nums[mid] > target:
                end = mid - 1  ## or end = mid
            elif nums[mid] < target:
                start = mid + 1  ## or start = mid

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end

        return -1


