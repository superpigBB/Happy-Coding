# Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).
#
# Example 1:
# Input: [3, 2, 1]
#
# Output: 1
#
# Explanation: The third maximum is 1.
# Example 2:
# Input: [1, 2]
#
# Output: 2
#
# Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
# Example 3:
# Input: [2, 2, 3, 1]
#
# Output: 1
#
# Explanation: Note that the third maximum here means the third maximum distinct number.
# Both numbers with value 2 are both considered as second maximum.


### Solution 1: wrong
# Runtime Error Message:# Line 9: IndexError: list index out of range
#  Last executed input: # [1,1,2]
class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return sorted(nums)[-1]
        return sorted(set(nums),reverse = True)[2]


# changed to => 57ms O(1) space, O(n) Time Complexity
class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(set(nums)) < 3:
            return sorted(nums)[-1]
        return sorted(set(nums),reverse = True)[2]

obj = Solution()
print(obj.thirdMax([3, 2, 1]))
print(obj.thirdMax([1, 2]))
print(obj.thirdMax([2, 2, 3, 1]))
print(obj.thirdMax([1, 3, 5, 6, 8, 8, 9, 13]))
print(obj.thirdMax([1,1,2]))
print ("\n")

### Solution 2: third max is to remove the first two max and then max the list is the third one
### Time O(N), space O(1)
class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(set(nums)) < 3:
            return max(nums)

        iter = 0
        num_set = set(nums)
        while iter < 2:
            num_set.remove(max(num_set))
            iter += 1
        return max(num_set)

obj = Solution()
print(obj.thirdMax([3, 2, 1]))
print(obj.thirdMax([1, 2]))
print(obj.thirdMax([2, 2, 3, 1]))
print(obj.thirdMax([1, 3, 5, 6, 8, 8, 9, 13]))
print(obj.thirdMax([1,1,2]))
print(obj.thirdMax([2,2,3,1]))
print("\n")


### Solution 3: without use any built-in function such as max and sorted
### Time O(N), space O(1)
### Actually it's not kind of fast, but just want to try this method just in case
class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = list(set(nums))[0]
        second = third = -float('inf')

        for num in list(set(nums))[1:]:
            # print (num)
            if num > first:
                third = second
                second = first
                first = num
                # print("first is ", first)
            elif num > second:
                third = second
                second = num
                # print ("second is ", second )
                # print("third is ", third)
            elif num > third:
                third = num
                # print("third is ", third)
        # print (first, second, third)
        if third == -float('inf'):
            return first
        else:
            return third


obj = Solution()
print(obj.thirdMax([3, 2, 1]))
print(obj.thirdMax([1, 2]))
print(obj.thirdMax([2, 2, 3, 1]))
print(obj.thirdMax([1, 3, 5, 6, 8, 8, 9, 13]))
print(obj.thirdMax([1,1,2]))
print(obj.thirdMax([2,2,3,1]))