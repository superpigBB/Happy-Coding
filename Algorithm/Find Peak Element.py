"""
Lintcode Version:

There is an integer array which has the following features:

The numbers in adjacent positions are different.
A[0] < A[1] && A[A.length - 2] > A[A.length - 1].
We define a position P is a peak if:

A[P] > A[P-1] && A[P] > A[P+1]
Find a peak element in this array. Return the index of the peak.

Example
Given [1, 2, 1, 3, 4, 5, 7, 6]

Return index 1 (which is number 2) or 6 (which is number 7)

Challenge
Time complexity O(logN)

Notice
It's guaranteed the array has at least one peak.
The array may contain multiple peeks, find any of them.
The array has at least 3 numbers in it.
"""

"""
思路过程：
相邻数两两不相等
first two 升序， last two 降序
找一个index p, 使得左边数和它比小，右边数和他比大
一个array可能有不止一个p, 只要找到其中一个就可以
=>根据已知条件，应可以把范围直接限制在index: 1 ~ len - 2
=>最直接做法：
    从 index 1到len-2一个个扫，看左右两边值和它对比是不是符合peak 条件，但这样time: O(N-2), space: O(1)
=>chanllenge: 用二分法去掉一半的解=> Time: O(log(n)), Space: O(1) 
=>比较难想到怎么用二分法？
"""
class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """

    """
    方法：因为对index是前是后没要求，那就随便划一半看看有没能找到peak
          => 因为array 两端的条件
          =>二分法：Time: O(log(N)), Space: O(1)
    """
    def findPeak(self, A):
        # write your code here
        ## corner cases => None

        start, end = 1, len(A) - 2
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] > A[mid - 1] and A[mid] > A[mid + 1]:
                return mid
            elif A[mid] < A[mid - 1]:
                end = mid - 1
            elif A[mid] < A[mid + 1]:
                start = mid + 1

        return end if A[start] < A[end] else start


#######################################################################################################################


"""
Leetcode Version:

A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.
Note:

Your solution should be in logarithmic complexity.
"""

"""
思路过程：
leetcode这题没有提两端的升序降序，只提了最后一个数是负无穷大，所以肯定有峰值
所以在start, end值方面不能直接忽略两端的值！ 

也是同样的搜索方法：二分法 => Time: O(log(N））, Space: O(1)

"""
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## corner cases
        if nums is None or len(nums) == 0:
            return 'Not found'
        if len(nums) == 1:
            return 0

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid - 1]:
                end = mid - 1
            elif nums[mid] < nums[mid + 1]:
                start = mid + 1

        return start if nums[start] > nums[end] else end

