# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
#
# Given two integers x and y, calculate the Hamming distance.
#
# Note:
# 0 ≤ x, y < 231.
#
# Example:
#
# Input: x = 1, y = 4
#
# Output: 2
#
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
#
# The above arrows point to positions where the corresponding bits are different.

### Solution 1: use bit calculation method to compare x % 2 and y % 2, once different, then difference count +1
### Time Complexity O(logN), Space Complexity O(1)

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        diff_cnt = 0
        while x!= 0 or y !=0 :
            if x % 2 != y % 2:
                diff_cnt += 1
            x = x // 2
            y = y // 2
        return diff_cnt

print(Solution().hammingDistance(1,4)) #2

### Solution 2: use bit calculation method in python to directly compare diff between binary x and y and count difference
### online solution! but it seems another way to compare
### Time Complexity O(N), Space Complexity O(1)

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x^y).count('1')
print(Solution().hammingDistance(1,4)) #2