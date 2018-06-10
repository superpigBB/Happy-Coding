#
# Given an integer array, sort it in ascending order. Use quick sort, merge sort, heap sort or any O(nlogn) algorithm
#
# Example
# Given [3, 2, 1, 4, 5], return [1, 2, 3, 4, 5].
#


### Solution 1: quick sort
### divide and conquer / recursion => Time Complexity O(NlogN), Space O(1)

class Solution:
    """
    @param A: an integer array
    @return: nothing
    """

    ### quick sort
    def sortIntegers2(self, A):
        # write your code here
        if len(A) == 0 or len(A) == 1:
            return

        ## quicksort divide and conquer
        self.quicksort(A, 0, len(A) - 1)

    def quicksort(self, A, start, end):
        ### termination condition for a recursion
        if start >= end:
            return

        left, right = start, end

        pivot = A[(left + right) / 2]

        while left <= right:
            while left <= right and A[left] < pivot:
                left += 1

            while left <= right and A[right] > pivot:
                right -= 1

            if left <= right:
                tmp = A[left]
                A[left] = A[right]
                A[right] = tmp

                right -= 1
                left += 1

        self.quicksort(A, start, right)
        self.quicksort(A, left, end)


### Solution2: merge sort
### divide and conquer / recursion => Time Complexity O(NlogN), Space O(N)

class Solution:
    """
    @param A: an integer array
    @return: nothing
    """

    ### merge sort
    def sortIntegers2(self, A):
        if A is None or len(A) == 0 or len(A) == 1:
            return

        newlist = [0] * len(A)
        self.mergeSort(A, 0, len(A) - 1, newlist)

    def mergeSort(self, A, start, end, newlist):
        if start >= end:
            return

        mid = (start + end) / 2

        self.mergeSort(A, start, mid, newlist)
        self.mergeSort(A, mid + 1, end, newlist)

        self.merge(A, start, mid, end, newlist)

    def merge(self, A, start, mid, end, newlist):
        left = start
        right = mid + 1
        index = start

        while left <= mid and right <= end:
            if A[left] <= A[right]:
                newlist[index] = A[left]
                left += 1
            else:
                newlist[index] = A[right]
                right += 1

            index += 1

        while left <= mid:
            newlist[index] = A[left]
            left += 1
            index += 1

        while right <= end:
            newlist[index] = A[right]
            index += 1
            right += 1

        for index in range(start, end + 1):
            A[index] = newlist[index]