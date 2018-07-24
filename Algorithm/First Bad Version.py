# Lintcode
#
#
# Description
# The code base version is an integer start from 1 to n. One day, someone committed a bad version in the code case, so it
# caused this version and the following versions are all failed in the unit tests. Find the first bad version.
#
# You can call isBadVersion to help you determine which version is the first bad one. The details interface can be found
# in the code's annotation part.
#
# Please read the annotation in code area to get the correct way to call isBadVersion in different language.
# For example, Java is SVNRepo.isBadVersion(v)
#
#
# Example
# Given n = 5:
#
# isBadVersion(3) -> false
# isBadVersion(5) -> true
# isBadVersion(4) -> true
# Here we are 100% sure that the 4th version is the first bad version.
#
# Challenge
# You should call isBadVersion as few as possible.

"""
class SVNRepo:
    @classmethod
    def isBadVersion(cls, id)
        # Run unit tests to check whether verison `id` is a bad version
        # return true if unit tests passed else false.
You can use SVNRepo.isBadVersion(10) to check whether version 10 is a
bad version.
"""


## 因为version是有序的，而且找第一个的系列，一般用Binary search
## 二分位置是中间的那个id，如果bad, end = mid; or: start = mid + 1
## Time: O(logn), Space: O(1)
class Solution:
    """
    @param: n: An integer
    @return: An integer which is the first bad version.
    """

    def findFirstBadVersion(self, n):
        # write your code here
        start = 1
        end = n

        while start + 1 < end:
            mid = start + (end - start) // 2
            if SVNRepo.isBadVersion(mid):
                end = mid
            else:
                start = mid + 1  # or start = mid

        if SVNRepo.isBadVersion(start):
            return start

        if SVNRepo.isBadVersion(end):
            return end

        return -1

# --------------------------------------------------------------------------------------------------------------------------------------------------------------\
#
# LeetCode
#
#
#
# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of
# your product fails the quality check. Since each version is developed based on the previous version, all the versions
# after a bad version are also bad.
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
#
# You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find
# the first bad version. You should minimize the number of calls to the API.
#
# Example:
#
# Given n = 5, and version = 4 is the first bad version.
#
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
#
# Then 4 is the first bad version.


## Solution is the same as Lintcode one





