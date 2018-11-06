"""
Given a mountain sequence of n integers which increase firstly and then decrease, find the mountain top.

Example
Given nums = [1, 2, 4, 8, 6, 3] return 8
Given nums = [10, 9, 8, 7], return 10
"""

"""
思路过程：
increase first, then decrease =>问题是：既然是山并且基于example, 也就是有
可能这个山只有increase array or decrease array？ =>觉得是
=>find the max of the list
1) if no time complexity requirement, the easiest way: one pointer =>
    time: O(N), Space: O(1)
2) faster way：binary search => time: O(log(N)), Space: O(1)

"""


class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    """
    Time: O(log(N))
    Space: O(1)
    """

    def mountainSequence(self, nums):
        # write your code here
        ## corner cases
        if nums is None or len(nums) == 0:
            return None
        if len(nums) == 1:
            return nums[0]

        start, end = 0, len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            ## mid_next = mid + 1
            if nums[mid] < nums[mid + 1]:  ## 跟后面那个比，没必要前后都比=>跟前面比可能出现没数的情况
                start = mid + 1
            elif nums[mid] > nums[mid + 1]:
                end = mid
            """可以问下有没可能升序或降序里面出现相等的情况
               在这里我默认觉得是没有这种情况，所以没有判断==的情况 
            """
        return max(nums[start], nums[end])
        ## OR
        # return nums[start] if nums[start] > nums[end]  else nums[end]








