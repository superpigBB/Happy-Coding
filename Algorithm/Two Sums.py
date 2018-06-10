# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

### Original Method: using list index O(N)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.num_list = nums
        self.target   = target

        found = 0
        for i in range(len(self.num_list)):
            num1 = self.num_list[i]
            num2 = self.target - num1
            try:
                j = self.num_list.index(num2)
            except:
                # print "can't find num2, we need to continue!"
                pass
            else:
                if i != j:
                    found = 1
                    return[i, j]
                    break
        if found == 0:
            print "No solution found!"



### Improved Solution: one time hash O(N) => faster
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        found = 0
        for i in xrange(len(nums)):
            a = nums[i]
            b = target - a
            if dict.has_key(b):
                found = 1
                return [dict[b], i]
            dict[a] = i
        if found == 0:
            print "No Solution Found!"


### Method 3: try enumerate to replace xrange

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        found = 0
        for i, value in enumerate(nums):
            v2 = target - value
            if dict.has_key(v2):
                found = 1
                return [dict[v2], i]
            dict[value] = i
        if found == 0:
            print "No Solution found"


### Method 4: try use in dict instead of dict.has_key()

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        found = 0
        for i, value in enumerate(nums):
            v2 = target - value
            if v2 in dict:
                found = 1
                return [dict[v2], i]
            dict[value] = i
        if found == 0:
            print "No Solution found"


x = Solution()
print x.twoSum([2, 7, 11, 15], 22)


### Conclusion:
### No matter enumerate or xrange, the key to make faster is
### "if key in dict" since it's kind of dict look up
### while "if key in dict.has_keys()" generates a list, lookup in a list is kind of slower than directly check dict itself