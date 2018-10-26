# Description
# Given a target number, a non-negative integer k and an integer array A sorted in ascending order, find the k closest numbers
# to target in A, sorted in ascending order by the difference between the number and target. Otherwise, sorted in
# ascending order by number if the difference is same.
#
# The value k is a non-negative integer and will always be smaller than the length of the sorted array.
# Length of the given array is positive and will not exceed 10^4
# Absolute value of elements in the array and x will not exceed 10^4
#
# Example
# Given A = [1, 2, 3], target = 2 and k = 3, return [2, 1, 3].
#
# Given A = [1, 4, 6, 8], target = 3 and k = 3, return [4, 1, 6].
#
# Challenge
# O(logn + k) time complexity.

### Lintcode Version
class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """

    ### sorted array, target value =>  compare absolute values OR
    ### number it self if the same
    ### 先找到last position <= target OR first position >= target
    ### 然后根据那个position，比较两边的值，然后直到找到第k个
    ### Time: O(logN+k), Space: O(k) => 建了个长度为K的list
    def kClosestNumbers(self, A, target, k):
        # write your code here
        ## corner cases
        if A is None or len(A) == 0:
            return []

        ## find last position in a list <= target
        index = self.findLastPosition(A, target)
        if index == -1:  ## 找不到<= target的位置，那就定义最后一个位置
            return A[0:k]

        ## compare numbers on left and right side of the indexed number
        ## and until k numbers in a list
        outputList = self.getTopK(A, target, [], index, index + 1, k)
        return outputList

    def findLastPosition(self, nums, target):
        start, end = 0, len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2

            if nums[mid] <= target:
                start = mid
            else:
                end = mid - 1

        if nums[end] <= target:
            return end
        else:
            return start
        return -1

    def getTopK(self, nums, target, outputList, left, right, k):
        cnt = 0  # count numbers in outputList
        while cnt < k:
            ### 写法1：
            if left >= 0 and right < len(nums) and target - nums[left] <= nums[right] - target:
                outputList.append(nums[left])
                left -= 1
            elif left >= 0 and right < len(nums) and target - nums[left] > nums[right] - target:
                outputList.append(nums[right])
                right += 1
            elif left >= 0:
                outputList.append(nums[left])
                left -=1
            elif right < len(nums):
                outputList.append(nums[right])
                right += 1
            ### OR：
            ### 写法2：
            if right >= len(nums):
                outputList.append(nums[left])
                left -= 1
            elif left < 0:
                outputList.append(nums[right])
                right += 1
            else:
                if target - nums[left] <= nums[right] - target:
                    outputList.append(nums[left])
                    left -= 1
                else:
                    outputList.append(nums[right])
                    right += 1

            cnt += 1

        return outputList

########################################################################################################################

### Leetcode Version: the only difference is return format: 估计Leetcode要用Priority queue => heap 来解决问题
# Given a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be
# sorted in ascending order. If there is a tie, the smaller elements are always preferred.
#
# Example 1:
# Input: [1,2,3,4,5], k=4, x=3
# Output: [1,2,3,4]
# Example 2:
# Input: [1,2,3,4,5], k=4, x=-1
# Output: [1,2,3,4]
# Note:
# The value k is positive and will always be smaller than the length of the sorted array.
# Length of the given array is positive and will not exceed 104
# Absolute value of elements in the array and x will not exceed 104
# UPDATE (2017/9/19):
# The arr parameter had been changed to an array of integers (instead of a list of integers). Please reload the code
# definition to get the latest changes.


### the only difference here from Lintcode version is the output should be sorted n ascending order

### Solution1: 利用了sublist的原理，成功减小了时间复杂度和空间复杂度，更优的解法！
########################################################################################################################
# the only difference here from Lintcode version is the output should be sorted n ascending order
# => 由于数组是有序的，所以最后返回的k个元素也一定是有序的，那么其实就是返回了原数组的一个长度为k的sublist
# => 对于sublist, start 要么就是起点0 或者是len(list) - k=>在这个基础上再进行二分，这样时间复杂度就直接变成O(log(n-k))
# Time Complexity: O(log(n-k)), Spacke Complexity: O(1)

class Solution:

    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if arr is None or len(arr) == 0:
            return []

        ## start index range
        start, end = 0, len(arr) - k

        ## binary search to locate start index
        while start < end:
            mid = (start + end) // 2
            ## compare distnace of first window size of k with second window size of k
            if abs(x - arr[mid]) < abs(arr[mid + k] - x):
                end = mid
            elif abs(x - arr[mid]) == abs(arr[mid + k] - x):
                ##距离相等情况下选小的
                end = mid  ## 第一个statement和第二个statement 实际可以合并
            else:  ## 第二个window的差值比较小
                start = mid + 1  ## 防止死循环
            # print("start:{}, mid:{}, end:{}".format(arr[start], arr[mid], arr[end]))
        return arr[start:start + k]

################ OR: while loop 也可以这么写，和九章模板类似来避免死循环##################################
###################################################################################################

        while start < end - 1:
            mid = (start + end ) // 2
            ## compare distnace of first window size of k with second window size of k
            if abs(x - arr[mid]) < abs(arr[mid+k] - x):
                end = mid
            elif abs(x - arr[mid]) == abs(arr[mid+k] - x):
                ##距离相等情况下选小的
                end = mid ## 第一个statement和第二个statement 实际可以合并
            else: ## 第二个window的差值比较小
                start = mid
            print("start:{}, mid:{}, end:{}".format(arr[start], arr[mid], arr[end]))

        ## 循环结束start = end - 1 and compare start/end哪个离x最近
        if start == end:
            return arr[start:start+k]
        elif abs(arr[start] - x) <= abs(arr[start + k] - x):
            return arr[start: start+k]
        else:
            return arr[end: end+k]


###Solution 2： 和lintcode一样的解法，只是最后利用index而不是新建List=>节省了space
###Time: O(logn + k), Space: O(1)
########################################################################################################################
class Solution:

    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if arr is None or len(arr) == 0:
            return []

        ## find last position in a list <= target
        index = self.findLastPosition(arr, x)
        if index == -1:  ## 找不到<= target的位置，那就定义最后一个位置
            return arr[0:k]

        ## compare numbers on left and right side of the indexed number
        ## and until k numbers in a list
        outputList = self.getTopK(arr, x, [], index, index + 1, k)
        return outputList

    def findLastPosition(self, nums, target):
        start, end = 0, len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2

            if nums[mid] <= target:
                start = mid
            else:
                end = mid - 1

        if nums[end] <= target:
            return end
        else:
            return start
        return -1

    def getTopK(self, nums, target, outputList, left, right, k):
        cnt = 0  # count numbers in outputList
        while cnt < k:
            ### 写法1：
            # if left >= 0 and right < len(nums) and target - nums[left] <= nums[right] - target:
            #     outputList.append(nums[left])
            #     left -= 1
            # elif left >= 0 and right < len(nums) and target - nums[left] > nums[right] - target:
            #     outputList.append(nums[right])
            #     right += 1
            # elif left >= 0:
            #     outputList.append(nums[left])
            #     left -=1
            # elif right < len(nums):
            #     outputList.append(nums[right])
            #     right += 1
            ### OR：
            ### 写法2：
            if right >= len(nums):
                # outputList.append(nums[left])
                left -= 1
            elif left < 0:
                # outputList.append(nums[right])
                right += 1
            else:
                if target - nums[left] <= nums[right] - target:
                    # outputList.append(nums[left])
                    left -= 1
                else:
                    # outputList.append(nums[right])
                    right += 1

            cnt += 1
        # print (left + 1 , right)
        return nums[left + 1: right]





