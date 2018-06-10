# Given an array nums of integers and an int k, partition the array (i.e move the elements in "nums") such that:
#
# All elements < k are moved to the left
# All elements >= k are moved to the right
# Return the partitioning index, i.e the first index i nums[i] >= k.
#
#  Notice
# You should do really partition in array nums instead of just counting the numbers of integers smaller than k.
#
# If all elements in nums are smaller than k, then return nums.length
#
#
# Example
# If nums = [3,2,2,1] and k=2, a valid answer is 1.
#


### Solution 1
### use quickSort的思想，得到Time O(N), Space O(1)
class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """

    ### use quickSort的思想，得到Time O(N), Space O(1)
    def partitionArray(self, nums, k):
        # write your code here
        ## 判断异常值
        if nums is None:
            return -1

        ## 类quicksort algorithm
        start, end = 0, len(nums) - 1
        ## 移动指针
        left, right = start, end
        pivot_value = k

        while left <= right:
            while left <= right and nums[left] < pivot_value:
                left += 1

            while left <= right and nums[right] >= pivot_value:
                right -= 1

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        ## left is the first index for nums[i] >= l
        return left