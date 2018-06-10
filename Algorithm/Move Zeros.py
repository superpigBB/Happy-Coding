# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
#
# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
# Credits:
# Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.


## Solution 1: 直接把非0的放前面部分list, 0 放list 后面部分 =》recommeded！ 因为需要变动次数相对最少
### Time Complexity O(N) Space Complexity O(1)
class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """

    def moveZeroes(self, nums):
        # write your code here
        ## corner cases
        if nums is None or len(nums) == 0 or len(nums) == 1:
            return

        i = 0
        zeroCnt = 0
        for num in nums:
            if num == 0:
                zeroCnt += 1
            else:
                nums[i] = num
                i += 1

        nums[i:] = [0] * zeroCnt


## OR

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nonzeroes = [x for x in nums if x != 0]
        if nonzeroes and len(nonzeroes) < len(nums):
            nums[:len(nonzeroes)] = nonzeroes
            nums[len(nonzeroes):] = [0] * (len(nums) - len(nonzeroes))


### Solution 2: two pointers
### Time Complexity O(N) Space Complexity O(1)
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0

        while j < len(nums):
            if nums[j] != 0:
                tmp = nums[j]
                nums[j] = nums[i] ## or nums[i], nums[j] = nums[j], nums[i]
                nums[i] = tmp
                i += 1
            j += 1


print(Solution().moveZeroes([0, 1, 0, 3, 2])) # [1, 3, 2, 0, 0]
print(Solution().moveZeroes([0])) #[0]
print(Solution().moveZeroes([0,0,1])) #[1,0,0]
print(Solution().moveZeroes([2, 1])) #[2,1]
print(Solution().moveZeroes([1,0,1])) #[2,1]
print(Solution().moveZeroes([4,2,4,0,0,3,0,5,1,0])) #[4,2,4,3,5,1,0,0,0]
print(Solution().moveZeroes([0,0])) #[0,0]
print("\n")


### Solution3: when 0s pop out and append 0s to the end of list
### Time Complexity O(N^2) Space Complexity O(1)
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        empty_cnt = nums.count(0)
        cnt = 0
        while i < len(nums):
            if nums[i] == 0:
                cnt += 1
                nums.pop(i) ##时间复杂度是O(N)
                nums.append(0)
                if cnt > empty_cnt:
                    i += 1
            # print(nums)

            else:
                i += 1


# print(Solution().moveZeroes([0, 1, 0, 3, 2])) # [1, 3, 2, 0, 0]
# print(Solution().moveZeroes([0])) #[0]
# print(Solution().moveZeroes([0,0,1])) #[1,0,0]
# print(Solution().moveZeroes([2, 1])) #[2,1]
# print(Solution().moveZeroes([1,0,1])) #[2,1]
# print(Solution().moveZeroes([4,2,4,0,0,3,0,5,1,0])) #[4,2,4,3,5,1,0,0,0]
# print(Solution().moveZeroes([0,0])) #[0,0]
# print("\n")






