"""
Given a sorted array of n integers, find the starting and ending position of a given target value.

If the target is not found in the array, return [-1, -1].

Example
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].

Challenge
O(log n) time.
"""

"""
思路过程：
sorted array n =>是不是有duplicates? =>看例子好像有
return: [start, end] or [-1, -1] if not found 
因为时间限定是log(n)，所以首先想到的是二分法
否则可以用O（n）时间解决这种题也可以
1 2 5 7 8 8 8 8 10

"""

class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """

    """
    找first position of target value and then 找last position of target value?
    Time: O(log(n)), Space: O(1)
    """

    def searchRange(self, A, target):
        # write your code here
        ## corner cases
        if A is None or len(A) == 0:
            return [-1, -1]

        ## find first position of the target
        if self.binarySearch(0, len(A) - 1, target, A, 1) is None:
            return [-1, -1]
        else:
            first_index = self.binarySearch(0, len(A) - 1, target, A, 1)

        ## find last position of the target
        if self.binarySearch(first_index, len(A) - 1, target, A, -1) is None:
            return [-1, -1]
        else:
            last_index = self.binarySearch(first_index, len(A) - 1, target, A, -1)

        return [first_index, last_index]

    def binarySearch(self, start, end, target, A, position):
        while start + 1 < end:
            mid = (start + end) // 2

            if A[mid] == target:
                if position == 1:
                    end = mid
                else:
                    start = mid
            elif A[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
            # print('in the loop, start = {}, end = {}'.format(start, end))

        print('start: {}, end: {}'.format(start, end))
        if position == 1:
            if A[start] == target:
                index = start
            elif A[end] == target:
                index = end
            else:
                index = None
        else:
            if A[end] == target:
                index = end
            elif A[start] == target:
                index = start
            else:
                index = None

        # print('index is', index)
        return index


