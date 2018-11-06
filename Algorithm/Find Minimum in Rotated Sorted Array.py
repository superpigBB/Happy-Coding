"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2]
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0

"""
"""
思路过程：
sorted array => rotated: Lintcode这题没讲升序还是降序！ 如果面试要问清楚！ 因为做法不一样！
0, 1, 2 | 4, 5, 6, 7 => 4, 5, 6, 7 | 0, 1, 2
find min number
=>要弄清楚的：有没有duplicate？ 特殊情况可能有0，1, 2, 4, 5, 6, 7
也有可能list为空或不存在
"""


class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    """
    思路过程：
    sorted array => rotated: 这题没讲升序还是降序！ 如果面试要问清楚！ 因为做法不一样！
    0, 1, 2 | 4, 5, 6, 7 => 4, 5, 6, 7 | 0, 1, 2
    find min number
    =>要弄清楚的：有没有duplicate？ 特殊情况可能有0，1, 2, 4, 5, 6, 7
    也有可能list为空或不存在
    """

    def findMin(self, nums):
        # write your code here
        ## corner cases
        if nums is None or len(nums) == 0:
            return None
        if len(nums) == 1:
            return nums[0]

        LastNum = nums[-1]
        start, end = 0, len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] == LastNum:  ## 可以把第一个if和第二个elif并一起如果为了简洁 nums[mid] <= LastNum
                end = mid
            elif nums[mid] < LastNum:
                end = mid
            else:
                start = mid + 1

        if nums[start] <= LastNum:  ## 或写成 return min(nums[start], nums[end])
            return nums[start]
        if nums[end] <= LastNum:
            return nums[end]
        return None





