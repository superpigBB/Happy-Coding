# Window Sum
# Given an array of n integer, and a moving window(size k), move the window at each iteration from the start of the array,
# find the sum of the element inside the window at each moving.
#
# Example
# For array [1,2,7,8,5], moving window size k = 3.
# 1 + 2 + 7 = 10
# 2 + 7 + 8 = 17
# 7 + 8 + 5 = 20
# return [10,17,20]

## Solution1: 更直白一点，先建一个长度为n-k+1的list, 这样就能save上一个sum是多少了
## 分两个loop =》 比 Solution2稍微快一点
## 极端情况也是O(N) 或 O(K)
## Time O(N) Space O(N)
class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """

    def winSum(self, nums, k):
        # write your code here
        ## corner cases
        if nums is None or len(nums) == 0:
            return nums
        if k >= len(nums):
            return [sum(nums)]

        ## initialize resultList with all 0s
        resultList = (len(nums) - k + 1) * [0]

        ## get first k sum
        for i in range(k):
            resultList[0] += nums[i]

        ## 规律就是：sum[2] = sum[1] - sum[i - 1] + nums[j]
        ## j = k + i - 1
        for i in range(1, len(nums) - k + 1):
            # j = k + i - 1
            resultList[i] = resultList[i - 1] + nums[k + i - 1] - nums[i - 1]

        return resultList

class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """

    ## Solution2. 同向双指针： 和solution 1基本属于一致，复杂度也是，极端的就是O(N）或 O(K)
    ## Time： O（NK）
    def winSum(self, nums, k):
        # write your code here
        ## corner cases
        if k == 1 or len(nums) == 0:
            return nums
        if k >= len(nums):
            return [sum(nums)]

        ## initialize result list/previous sum
        resultList = []
        currentSum = 0
        # previousStartIndex = 0

        ## initialize j: moving pointer
        j = 0
        for i in range(len(nums) - k + 1):
            while j <= k + i - 1 and j < len(nums):
                currentSum += nums[j]
                j += 1

            if i != 0:
                currentSum -= nums[i - 1]
            # previousStartIndex = i

            resultList.append(currentSum)

        return resultList



