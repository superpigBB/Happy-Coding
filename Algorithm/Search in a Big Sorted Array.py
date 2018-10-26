# Description
# Given a big sorted array with positive integers sorted by ascending order. The array is so big so that you can not get
# the length of the whole array directly, and you can only access the kth number by ArrayReader.get(k)
# (or ArrayReader->get(k) for C++). Find the first index of a target number.
#  Your algorithm should be in O(log k), where k is the first index of the target number.
#
# Return -1, if the number doesn't exist in the array.
#
# If you accessed an inaccessible index (outside of the array), ArrayReader.get will return 2,147,483,647.
#
# Have you met this question in a real interview?
# Example
# Given [1, 3, 6, 9, 21, ...], and target = 3, return 1.
#
# Given [1, 3, 6, 9, 21, ...], and target = 4, return -1.
#
# Challenge
# O(log k), k is the first index of the given target number.


"""
思路过程：
sorted Array =>ascending
positive integer
big
len unknown
index and get value only
first index of a target number
time: O(logk)
0,...k, ...,inf

0..|.k
"""


class Solution:
    """
    @param: reader: An instance of ArrayReader.
    @param: target: An integer
    @return: An integer which is the first index of target.
    """
    """
    因为不知道list长度，所以无法用（start + end） // 2 来得出中点值，所以只能用先用倍增法快速得到第一个>= target的k， 然后再用二分法
    来判断具体target所在的index位置
     Time: O(2*O(logK)), Space: O(1)
    """

    def searchBigSortedArray(self, reader, target):
        # write your code here
        ## corner cases
        if reader.get(0) == target:
            return 0

        start, k = 0, 1
        ## find k => time: O(log(k))
        while reader.get(k) < target:
            k = k * 2
            # print("k is {}, value is {}".format(k, reader.get(k)))

        ## k is the first index whose value >= target
        ## implement 二分法
        while start + 1 < k:
            mid = (start + k) // 2

            if reader.get(mid) == target:
                k = mid
            elif reader.get(mid) < target:
                start = mid + 1
            else:
                k = mid - 1

        if reader.get(start) == target:
            return start
        if reader.get(k) == target:
            return k

        return -1