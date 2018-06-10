# Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
#
# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.
#  Please note that your returned answers (both index1 and index2) are not zero-based.
#
# You may assume that each input would have exactly one solution and you may not use the same element twice.
#
# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2
#

## Original Method
# at first not consider [-1, 0] -1 situation: [-3, -2], -5,   [-3, 1], -2
# that's why I choose the sae Two Sums script to do that, but with running time 39s, while the best running time is 28s
# According to answer, I may apply two pointers to solve the problem

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}

        for i in xrange(len(numbers)):
            num1 = numbers[i]
            num2 = target - num1
            if num2 in dict:
                return [dict[num2] + 1, i + 1]
            dict[num1] = i

## Method 2: try to eliminate some variables and try whether speed is improved
## it improves by elimiating variables to 33s
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in xrange(len(numbers)):
            if target - numbers[i] in dict:
                return [dict[target - numbers[i]] + 1, i + 1]
            dict[numbers[i]] = i

### Method3: try two pointers which should be O(N) and O(1) for space, since no hash should be created, only two pointers in list
### 36s with space O(1) and time O(N)
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # corner case
        n = len(numbers)
        if n <= 1:
            return []

        i, j = 0, n - 1
        while i < j:
            sum = numbers[i] + numbers[j]
            if sum == target:
                return [i + 1, j + 1]
            elif sum > target:
                j -= 1
            else:
                i += 1



X = Solution()
print (X.twoSum([2, 7, 11, 15], 9))
print (X.twoSum([-1, 0], -1))