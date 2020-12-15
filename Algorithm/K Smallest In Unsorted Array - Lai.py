"""
Find the K smallest numbers in an unsorted integer list A. The returned numbers should be in ascending order.

Assumptions

A is not null
K is >= 0 and smaller than or equal to size of A
Return

an list with size K containing the K smallest numbers in ascending order
Examples

A = {3, 4, 1, 2, 5}, K = 3, the 3 smallest numbers are {1, 2, 3}
"""

"""
---------------------TO DO -------------------
解题思路：两种方法 
方法 1.quick select (reference 九章 Kth Largest Element in an list.py AND LaiOffer课) 
    但九章的这个方法只能只能第kth smallest值在哪儿不用反复排序，所以用quick select，然而这道题是需要
    return sorted smallest elements的，所以用max heap 更优
    Time: O(n + klogk) Space: O(k) 
方法 2.max heap 
"""



class Solution(object):
    """"""
    """
    方法 2. max heap
    解题思路：在一个unsorted array里面找K个有序数列，一般最快速是用堆HEAP;
    如果最小，那就用Max Heap=>可以相对容易知道在那个HEAP里哪个数最大，然后input只要比这个数小就进来，直到k个数在里面
    Time: O((n-k) * logk + k)
    Space: O(k)
    """

    def kSmallest2(self, array, k):
        """
        input: int[] array, int k
        return: int[]
        """
        # write your solution here
        # corner cases
        if array is None or len(array) == 0 or k <= 0 or len(array) < k:
            return []

        # 因为要用max heap， 所以所有数都要* -1
        import heapq
        heap = list()
        heapq.heapify(heap)

        for i in range(len(array)):
            # populate heap for the first k elements
            if i < k:
                heapq.heappush(heap, -array[i])
            else:
                # compare max and push element smaller than max and pop max
                if heap[0] < -array[i]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, -array[i])

        result = [0] * k
        for i in range(k - 1, -1, -1):
            result[i] = -1 * heapq.heappop(heap)

        return result

    """
    方法 1. quick select
    Time: O(n + klogk)
    Space: O(k)
    在找k smallest or largest题，最好用heap而不是quick select,除非问kth smallest/largest
    以下解法for kthlargest
    """
    def findKthLargest(self, nums, k):
        # # corner cases
        # if nums is None or len(nums) == 0:
        #     return -1  # assume -1 represents finding nothing
        return self.quickselect(nums, 0, len(nums) - 1, len(nums) - k)

    """Quick Select Function"""
    def quickselect(self, array, start, end, target_index):
        # base cases
        if start == end:
            return array[start]

        # define two moving pointers
        left, right = start, end
        # take middle index of array as pivot value
        mid = (start + end) // 2
        pivot_value = array[mid]

        # similar quickSort template for sorting left and right
        while left <= right:
            while left <= right and array[left] < pivot_value:
                left += 1

            while left <= right and array[right] > pivot_value:
                right -= 1

            if left <= right:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1

        """
           unlike quick sort, we only need to do quickselect on at most one partion 
           if the pivot is already the kth smallest element, we can directly return
        """
        if target_index <= right:   # only need to recursively call quick select on the left partition
            return self.quickselect(array, start, right, target_index)
        elif target_index >= left:    # only need to recursively call quick select on the right partition
            return self.quickselect(array, left, end, target_index)
        else:
            return array[target_index]


print(Solution().kSmallest([3, 1, 5, 2, 4], 4))    # [1, 2, 3, 4]
print(Solution().kSmallest([3, 4, 1, 2, 5], 3))    # [1, 2, 3]
print(Solution().kSmallest([3, 1, 5, 2, 4], 2))    # [1, 2]
