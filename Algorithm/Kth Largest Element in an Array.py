# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
# For example,
# Given [3,2,1,5,6,4] and k = 2, return 5.
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.

###Solution1: use set to remove k-1 max num
### Time O(KN), Space O(N)
### wrong! since it's not asked to find the kth distinct element
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        unique_nums = list(set(nums))

        if(len(unique_nums) < k):
            return max(unique_nums)

        for i in range(0, k-1):
            unique_nums.remove(max(unique_nums))
        return max(unique_nums)


# print(Solution().findKthLargest([3, 3, 3, 3, 4, 3, 3, 3, 3], 9)) #3
# print(Solution().findKthLargest([3,3,3,3,3,3,3,3,3], 8)) #3
# print(Solution().findKthLargest([1,1,2,5,3,3], 3)) #2
# print(Solution().findKthLargest([3,2,1,5,6,4], 2)) #5
# print(Solution().findKthLargest([1,1], 2)) #-1
# print("\n")
#

###Solution2: use remove k-1 max num
### Time O(NK), Space O(1)
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        for i in range(0, k-1):
            nums.remove(max(nums))
        return max(nums)


# print(Solution().findKthLargest([3, 3, 3, 3, 4, 3, 3, 3, 3], 9)) #3
# print(Solution().findKthLargest([3,3,3,3,3,3,3,3,3], 8)) #3
# print(Solution().findKthLargest([1,1,2,5,3,3], 3)) #3
# print(Solution().findKthLargest([3,2,1,5,6,4], 2)) #5
# print(Solution().findKthLargest([1,1], 2)) #1
# print("\n")


### Solution 3: 用quick select的algorithm， 前面那些的time complexity 都是kn, 如果k 很大就不乐观
### 我的方法相比九章的更直观
### quick select 算法的平均时间复杂度Time 为O(1), Space O(1)
class Solution:
    # @param k & A a integer and an array
    # @return ans a integer

    ## quick select algorithm with average time O(N), space O(1)
    def findKthLargest(self,  nums, k):
        ## 异常值检测
        if nums is None or k > len( nums):
            return -1

        ## quickSelect 调用
        self.quickSelect( nums, k - 1, 0, len( nums) - 1)
        # print( nums)
        return  nums[k - 1] ## or change to return self.quickSelect(nums, k - 1, 0, len( nums) - 1)

    ## define quickSelect function
    def quickSelect(self,  nums, index_aftersort, start, end):
        ## define termination condition
        if start >= end:
            return ## or change to return nums[start]

        ## define two moving pointers
        left, right = start, end
        ## take middle index of array as pivot value
        mid = (start + end) // 2
        pivot_value =  nums[mid]

        ## similar quickSort template for sorting left and right
        while left <= right:
            while left <= right and  nums[left] > pivot_value:
                left += 1

            while left <= right and  nums[right] < pivot_value:
                right -= 1

            if left <= right:
                 nums[left],  nums[right] =  nums[right],  nums[left]
                 left += 1
                 right -= 1

        ## to determine which half we should continue sorting and abandon another half
        ## left: [start, right], right: [left, end], middle:  nums[right + 1] or not exist => totally 3 parts
        if index_aftersort <= right:
            self.quickSelect( nums, index_aftersort, start, right) # or change to return self.quickSelect( nums, index_aftersort, start, right)

        elif index_aftersort > left:
            self.quickSelect( nums, index_aftersort, left, end) # or change to return self.quickSelect( nums, index_aftersort, left, end)

        else:
            return  nums[right + 1]



### Solution 3.1 quick select but using jiuzhang method
class Solution:
    # @param k & A a integer and an array
    # @return ans a integer

    ## quick select algorithm with average time O(N), space O(1)
    def findKthLargest(self,  nums, k):
        ## 异常值检测
        if nums is None or k > len( nums):
            return -1

        ## quickSelect 调用
        return self.quickSelect( nums, k,  0, len( nums) - 1)


    ## define quickSelect function
    def quickSelect(self,  nums, k , start, end):
        ## define termination condition
        ## 如果满足这个值说明找到并返回值
        if start >= end:
            return nums[start]

        ## define two moving pointers
        left, right = start, end
        ## take middle index of array as pivot value
        mid = (start + end) // 2
        pivot_value =  nums[mid]

        ## similar quickSort template for sorting left and right
        while left <= right:
            while left <= right and  nums[left] > pivot_value:
                left += 1

            while left <= right and  nums[right] < pivot_value:
                right -= 1

            if left <= right:
                 nums[left],  nums[right] =  nums[right],  nums[left]
                 left += 1
                 right -= 1

        ## to determine which half we should continue sorting and abandon another half
        ## left: [start, right], right: [left, end], middle:  nums[right + 1] or not exist => totally 3 parts
        if start + k - 1 <= right:
            return self.quickSelect( nums, k, start, right)

        elif start + k - 1 >= left:
            return self.quickSelect( nums, k - (left - start), left, end)

        else:
            return  nums[right + 1]

print(Solution().findKthLargest([3, 3, 3, 3, 4, 3, 3, 3, 3], 9)) #3
print(Solution().findKthLargest([3,3,3,3,3,3,3,3,3], 8)) #3
print(Solution().findKthLargest([1,1,2,5,3,3], 3)) #3
print(Solution().findKthLargest([3,2,1,5,6,4], 2)) #5
print(Solution().findKthLargest([1,1], 2)) #1
print("\n")
