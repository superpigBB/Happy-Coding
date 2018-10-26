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

    class Solution:
        """
        @param nums: a rotated sorted array
        @return: the minimum number in the array
        """
        """
        因为没有duplicate,所以解是唯一 =>如果有重复， 可能达不到log(n) 的时间复杂度，因为可能是1 1 1 1 1 1 0=> log(n)

        rotated也有可能在起点进行rotate, 这样就相当于直接的sorted array 
        =>正常来说，这个题要么就是求first position that >= first number
        或者：求first position that <= larst number

        => 但就因为还有种特殊情况：sorted array可能在第0个位置翻转，所以导致还可能是sorted array 0 1 2 3 4 5,...
        在这种情况下，如果用first position >= first number,就会导致死循环找不
        =>所以只能用first position <= last number来做！

        Time: O(log(N)), Space: O(1)
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
                if nums[mid] == LastNum:
                    end = mid
                elif nums[mid] < LastNum:
                    end = mid
                else:
                    start = mid + 1

            if nums[start] <= LastNum:
                return nums[start]
            if nums[end] <= LastNum:
                return nums[end]
            return None





