# Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#
# Note:
# You are not suppose to use the library's sort function for this problem.
#
# Follow up:
# A rather straight forward solution is a two-pass algorithm using counting sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
#
# Could you come up with an one-pass algorithm using only constant space?

### Solution 1: Count sort: use dict to save all numbers and their countings and then re-assign them to list according to sequence
### two loops: Time O(Nk) Space O(N)
### counting sort method
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) == 0 or len(nums) == 1:
            return

        ## create hash for saving nums
        nums_dict = {}
        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = 1
            else:
                nums_dict[num] += 1

        ## loop through three different colors
        index = 0  ## index of nums, to re-order number inside
        for color in [0, 1, 2]:
            if color not in nums_dict:
                continue
            while nums_dict[color] > 0:
                nums[index] = color
                index += 1
                nums_dict[color] -= 1


# print(Solution.sortColors([2,1,0,0,2,1]))  ##[0, 0, 1, 1, 2, 2]
# print('\n')

### Solution 2: partition twice and directly apply quick sort
### the answer is from online: jiuzhang algorithm website
### Time O(N), Space O(1)
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        self.quicksort(nums, 1, self.quicksort(nums, 0, 0))

    def quicksort(self, nums, pivot_val, startindex):
        start = startindex
        end = len(nums) - 1

        while start <= end:
            while start <= end and nums[start] == pivot_val:
                start += 1

            while start <= end and nums[end] != pivot_val:
                end -= 1

            if start <= end:
                tmp = nums[start]
                nums[start] = nums[end]
                nums[end] = tmp
                ## or we can directly write as nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        return start

# print(Solution().sortColors([2,1,0,0,2,1]))  ##[0, 0, 1, 1, 2, 2]
# print('\n')

### Solution 3: 三指针算法, 类似于quick sort但只要partition 一次就能排序完成
### Time Complexity O(N), Space O(1)

class Solution:
    ### three pointers algorithm
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        ## set 3 pointers left, right, i
        left = 0
        right = len(nums) - 1
        i = 0

        while i <= right:
            if nums[i] == 0:
                ## swap left and i to make 0s on left side or we can use swap(left, i)
                nums[left], nums[i] = nums[i], nums[left]
                i += 1
                left += 1

            elif nums[i] == 2:
                ## swap right and i to make 2s on right
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1

            ## if nums[i] == 1: pass
            else:
                i += 1

print(Solution().sortColors([2,1,0,0,2,1]))  ##[0, 0, 1, 1, 2, 2]
print('\n')




