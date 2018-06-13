# Description
# Given an array of integers, find two numbers that their difference equals to a target value.
# where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are NOT zero-based.

# Example
# Given nums = [2, 7, 15, 24], target = 5
# return [1, 2] (7 - 2 = 5)

## Hash is the best solution here => using Solution 1
class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """

    ## Solution 1: hash记录扫过的点:{value:index} => 这题用hash更优， 因为时间复杂度较低
    ## Time O(n), Space: O(n)
    def twoSum7(self, nums, target):
        # write your code here
        ## corner cases
        if nums is None or len(nums) == 0 or len(nums) == 1:
            return []

        ## initialize dict
        numsPast = {}

        for i in range(len(nums)):
            if (target + nums[i]) in numsPast:
                return [numsPast[target + nums[i]], i + 1]

            elif (-target + nums[i]) in numsPast:
                return [numsPast[-target + nums[i]], i + 1]

            numsPast[nums[i]] = i + 1

        return []

    ## Solution 2: 先排序再双指针 =》 如果排序好的话这题用双指针会快点
    ## Time O(nlogn), Space: O(n)
    def twoSum7(self, nums, target):
        # write your code here
        ## corner cases
        if nums is None or len(nums) == 0 or len(nums) == 1:
            return []

        ## 先把每个数的index存进dict里面
        from collections import defaultdict
        dict = defaultdict(list)  ## num : index
        for i in range(len(nums)):
            dict[nums[i]].append(i + 1)

        ## sort list first
        nums.sort()

        ## 因为排序了，所以两数之差肯定是正数
        target = abs(target)

        j = 1
        for i in range(len(nums)):
            while j < len(nums) and nums[j] - nums[i] < target:
                j += 1

            if j < len(nums) and nums[j] - nums[i] == target:
                ## get indexes for nums[j] and nums[i]
                if nums[j] == nums[i]:
                    return [dict[nums[i]][0], dict[nums[i]][1]]
                else:
                    if dict[nums[i]] > dict[nums[j]]:
                        return [dict[nums[j]][0], dict[nums[i]][0]]
                    else:
                        return [dict[nums[i]][0], dict[nums[j]][0]]

        return []

    ## Solution 2.2: 先排序再双指针 =》 如果排序好的话这题用双指针会快点 => 同Solution 2，只是用enumerate 代替dict
    ## Time O(nlogn), Space: O(n)
    def twoSum7(self, nums, target):
        # write your code here
        ## corner cases
        if nums is None or len(nums) == 0 or len(nums) == 1:
            return []

        ## enumerate nums 使之变成一个tuple (num, index)的形式，这样比起dict更容易表达出duplicate数的index
        nums = [(num, i + 1) for i, num in enumerate(nums)]
        ## sort list by first element in tuple first
        nums.sort(key=lambda x: x[0])

        ## 因为排序了，所以两数之差肯定是正数
        target = abs(target)

        ## initialize return result
        result = []

        j = 1
        for i in range(len(nums)):
            while j < len(nums) and nums[j][0] - nums[i][0] < target:
                j += 1

            if j < len(nums) and nums[j][0] - nums[i][0] == target:
                # print "i, j is %d, %d" %(i, j)
                if i == j:
                    continue
                result = [nums[i][1], nums[j][1]]
                break

        ## sort result[0], result[1]因为说了要从小到大
        if result[0] > result[1]:
            result[0], result[1] = result[1], result[0]

        return result