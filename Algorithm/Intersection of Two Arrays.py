# Given two arrays, write a function to compute their intersection.
#
# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].
#
# Note:
# Each element in the result must be unique.
# The result can be in any order.

## 四大solutions: 1) hashset 2) set operation 3) sort & merge 4) sort and binary search

class Solution:
    """
    @param: nums1: an integer array
    @param: nums2: an integer array
    @return: an integer array
    """

    ## Solution 1: hashset to record one of array, and if second one duplicate the
    ## same num#, then it's the intersection part
    ## Time: O(N), Space: O(N)
    def intersection(self, nums1, nums2):
        # write your code here
        ## corner cases
        if nums1 is None and nums2 is None:
            return []

        nums1Set = set(nums1)

        intersectSet = set()
        for num in set(nums2):
            if num in nums1Set and num not in intersectSet:
                intersectSet.add(num)

        return list(intersectSet)


    ## Solution 2: directly use set operations
    ## Time: O(N), Space: O(1)
    # if eg:
    #     >> >  # Demonstrate set operations on unique letters from two words
    #     ...
    #     >> > a = set('abracadabra')
    #     >> > b = set('alacazam')
    #     >> > a  # unique letters in a
    #     {'a', 'r', 'b', 'c', 'd'}
    #     >> > a - b  # letters in a but not in b
    #     {'r', 'd', 'b'}
    #     >> > a | b  # letters in a or b or both
    #     {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
    #     >> > a & b  # letters in both a and b
    #     {'a', 'c'}
    #     >> > a ^ b  # letters in a or b but not both
    #     {'r', 'd', 'b', 'm', 'z', 'l'}
    def intersection2(self, nums1, nums2):
        # write your code here
        return list(set(nums1) & set(nums2))