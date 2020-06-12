# Given an array of n objects with k different colors (numbered from 1 to k), sort them so that objects of the same color
# are adjacent, with the colors in the order 1, 2, ... k.
#
#  Notice
# You are not suppose to use the library's sort function for this problem.
#
# k <= n
#
# Example
# Given colors=[3, 2, 2, 1, 4], k=4, your code should sort colors in-place to [1, 2, 2, 3, 4].
#
# Challenge
# A rather straight forward solution is a two-pass algorithm using counting sort. That will cost O(k) extra memory.
# Can you do it without using extra memory?



### Solution 1: counting sort like Sort Colors, but time exceeded
### Time O(NK), Space O(N)
class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """

    ### Solution 1: using counting sort 计数排序
    def sortColors2(self, colors, k):
        # write your code here
        if colors is None or len(colors) == 0 or len(colors) == 1:
            return

        ## create hash for saving nums
        nums_dict = {}
        for num in colors:
            if num not in nums_dict:
                nums_dict[num] = 1
            else:
                nums_dict[num] += 1

        ## loop through k different colors
        color = 1
        index = 0  ## index of nums, to re-order number inside
        while color <= k:
            if color not in nums_dict:
                continue
            while nums_dict[color] > 0:
                colors[index] = color
                index += 1
                nums_dict[color] -= 1

            color += 1


### Solution 2: similar to quick sort, 把mid of 1~k 作为pivot value，然后把N个数分成左右两边
### combination of merge sort and quick sort
### Time Complexity O(Nlogk) Space O（1）
class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """

    def sortColors2(self, colors, k):
        # write your code here
        if k == 1 or len(colors) == 0 or len(colors) == 1 or colors is None:
            return

        self.rainbowSort(colors, 0, len(colors) - 1, 1, k)

    def rainbowSort(self, colors, start, end, colorfrom, colorto):
        ## termination condition
        if start >= end:
            return

        if colorfrom == colorto:
            return

        left, right = start, end
        ## choose pivot value, which should be the mid of start/end colors
        pivot_value = (colorfrom + colorto) / 2

        ## quick sort to get left part < pivot_value, right part > pivot_value
        while left <= right:
            while left <= right and colors[left] <= pivot_value:  ## 唯一和quick sort不一样的地方是这里colors[left] <= pivot_value而不应该是 < pivot_value，必须让一边完全<= pivot value，另一边没有pivot_value并大于
                left += 1

            while left <= right and colors[right] > pivot_value:
                right -= 1

            if left <= right:
                ## left and right exchange when found left value >= pivot_value and right value <= pivot_value
                colors[left], colors[right] = colors[right], colors[left]
                left += 1
                right -= 1

        # print ('left: color from %d color to %d' %(colorfrom, pivot_value))
        # print ('right: color from %d color to %d' %(pivot_value, colorto))

        self.rainbowSort(colors, start, right, colorfrom, pivot_value)
        self.rainbowSort(colors, left, end, pivot_value + 1, colorto)


### Solution 3: from jiuzhang solution 2, it might has the error of exceeding time but I need to know how to realize that
### Time Complexity O(KN), Space O（1）
class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """

    ### Solution 3: 类似于sort color的解法，三指针解法： 就是先每次loop出数组里最大和最小值，分别把他们放到数组的左边和右边，然后得到新的起始位置， 再做余下部分的同样操作，直到左边和右边相交
    ### 但这种方法可能会超时因为Time是O(NK), Space是O(1)
    def sortColors2(self, colors, k):
        # write your code here

        ## 判断异常值
        if colors is None or len(colors) == 0 or len(colors) == 1 or k == 1:
            return

        start, end = 0, len(colors) - 1
        ## 设置left, right 移动指针
        left, right = start, end

        ## set count how many colors have been sorted
        count = 0
        ## 每次循环是为了把当前left - right指向的数组的最小最大值分别扔到left和right边直到没有多余的k可以排
        while count < k:
            ##设置滑动指针 i, 指向起始点, 三指针loop
            i = left
            if left >= right:  ## k >=3 不可能有这种情况，除非k<=2
                return
            ### 设置min/max value of current searched arraylist
            current_min = min(colors[left:right + 1])
            current_max = max(colors[left:right + 1])

            while i <= right:
                if colors[i] == current_min:
                    colors[left], colors[i] = colors[i], colors[left]
                    i += 1
                    left += 1

                elif colors[i] == current_max:
                    colors[right], colors[i] = colors[i], colors[right]
                    right -= 1

                else:
                    i += 1

            ## 2 colors have been sorted, then we need to sort the rest
            count += 2


print (Solution().sortColors2([3,2,2,1,4], 4)) ## [1,2,2,3,4]
print('\n')