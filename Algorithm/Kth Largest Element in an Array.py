# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
# For example,
# Given [3,2,1,5,6,4] and k = 2, return 5.
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.
class Solution:
    """
    解题思路：用quick select， 一次quick sort然后看kth所在的range，对那个range进行排序就行
    Time: O(n)
    Space: O(1)
    """

    def findKthLargest(self, nums, k):
        # # corner cases
        # if nums is None or len(nums) == 0:
        #     return -1  # assume -1 represents finding nothing
        return self.quickselect(nums, 0, len(nums) - 1, len(nums) - k)

    """Quick Select Function"""
    def quickselect(self, array, start, end, target_index):
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
           if the pivot is already the kth smallest element, we can directly return
        """
        if target_index <= right:   # only need to recursively call quick select on the left partition
            return self.quickselect(array, start, right, target_index)
        elif target_index >= left:    # only need to recursively call quick select on the right partition
            return self.quickselect(array, left, end, target_index)
        else:
            return array[target_index]


print(Solution().findKthLargest([3, 3, 3, 3, 4, 3, 3, 3, 3], 9)) #3
print(Solution().findKthLargest([3,3,3,3,3,3,3,3,3], 8)) #3
print(Solution().findKthLargest([1,1,2,5,3,3], 3)) #3
print(Solution().findKthLargest([3,2,1,5,6,4], 2)) #5
print(Solution().findKthLargest([1,1], 2)) #1
print("\n")
