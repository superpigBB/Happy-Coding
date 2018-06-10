# Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.
#
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
#
# Example:
#
# Given nums = [1,1,2],
#
# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
# It doesn't matter what you leave beyond the new length.

### Original method: since it's sorted, we need to scan the whole array and only count those non-duplicate one
### Wrong!!! Since problem asks to remove the duplicates " in-place "!!! Which is very critical!!! the length is correct,
### but we still need to remove the duplicates in original array!!!


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        start = nums[0]
        unique_cnt = 1

        for num in nums[1:]:
            if num != start:
                unique_cnt += 1
                start = num
        return unique_cnt


### Method 2
### the only way we can use is two pointers i j, to move forward, and i to store count,
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        nums = nums[:i+1]
        # return i + 1
        return i + 1, nums
#
# obj = Solution()
# print(obj.removeDuplicates([1, 1, 2]))
# print(obj.removeDuplicates([]))
# print(obj.removeDuplicates([1,1,1]))
# print(obj.removeDuplicates([1, 1, 2, 3, 3, 5]))
### If array is not sorted

# Given an array of integers, remove the duplicate numbers in it.
#
# You should:
# 1. Do it in place in the array.
# 2. Move the unique numbers to the front of the array.
# 3. Return the total number of the unique numbers.

### Solution 1: delete duplicate and append that to the end of array use hash to judge
### O(n) time and O（n）space
class Solution:
    """
    @param: nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        dict = {}
        duplicate_cnt = 0
        for num in nums:
            dict.setdefault(num, 0)
            dict[num] +=1
        nums[:len(dict.keys())] = dict.keys()
        return len(dict.keys()), nums[:len(dict.keys()) ]

        # return len(nums) - duplicate_cnt, nums

### Solution 2: sort list first and then use two pointers
### O(nlogn) time, O(1) extra space
class Solution:
    """
    @param: nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        if len(nums) == 0:
            return 0
        ## sort in place
        nums.sort() ## if use sorted(nums) => create a new list

        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        nums = nums[:i+1]
        # return i + 1
        return i + 1, nums



obj = Solution()

## array not sorted
print(obj.deduplication([1,3,1,4,4,2]))