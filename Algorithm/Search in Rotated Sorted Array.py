"""
Lintcode Version:

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Example
For [4, 5, 1, 2, 3] and target=1, return 2.

For [4, 5, 1, 2, 3] and target=0, return -1.

Challenge
O(logN) time
"""

"""
思路过程：
rotated sorted array 1 2 3 4 5 is also another extreme case of that 
target => index or -1 if not found
no duplicates 

4 5 6 7 0 1 2 

0 1 2 4 5 6 7

两种方法这里！！！

方法一： 两次二分： 比较简单直接能想到
step 1 我觉得先求出最低点也就是Pivot的点在哪儿=>从而可以确定最小值和最大值是什么以及相关位置
setp2 把pivot较小端的最大值和较大list的最小值进行比较
    =>以确定在哪儿段去找target值
    
Time: O(log(N)), Space: O(1)


这题还可以用一次二分解决！得再看看！ mark！
"""

class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        # write your code here
        ## corner cases
        if A is None or len(A) == 0:
            return -1

        ## 找最低点=>得到两个range:第一个比最后一个数小的位置(从前往后)
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            """
            第一第二个statements可以合并为一个
            """
            if A[mid] == A[-1]:
                end = mid
            elif A[mid] < A[-1]:
                end = mid
            else:
                start = mid + 1

        range_start = start if A[start] < A[-1] else end
        """
        可能两个range: 1) range_start - A[-1]
                       2）0 - range_start - 1 
        """
        if range_start > 0 and target >= A[0] and target <= A[range_start - 1]:
            return self.target_search(A, 0, range_start - 1, target)
        elif target >= A[range_start] and target <= A[len(A) - 1]:
            return self.target_search(A, range_start, len(A) - 1, target)
        else:
            return -1

    def target_search(self, A, start, end, target):
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] == target:
                return mid
            elif A[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1



    """
    方法二:
    思路过程：一次二分！
    eg. 4 5 6 7 0 1 2 

    eg. 0 1 
    看mid划在哪里从而确定一半范围

    没有第一个方法：二次二分直接
    但时间复杂度稍微好点

    """

    def search2(self, A, target):
        # write your code here
        ## corner cases
        if A is None or len(A) == 0:
            return -1

        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2

            if A[mid] == target:
                return mid
                ## 看到底mid划在了上升区间
            if A[mid] >= A[start]:
                if target >= A[start] and target <= A[mid]:
                    end = mid
                else:
                    start = mid + 1

                    # if A[mid] < A[start]:
            else:
                if target >= A[mid] and target <= A[end]:
                    start = mid
                else:
                    end = mid - 1

        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1






