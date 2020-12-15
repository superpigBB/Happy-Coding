"""
Given an list of balls, where the color of the balls can only be Red, Green or Blue,
sort the balls such that all the Red balls are grouped on the left side,
all the Green balls are grouped in the middle and all the Blue balls are grouped on the right side.
(Red is denoted by -1, Green is denoted by 0, and Blue is denoted by 1).

Examples

{0} is sorted to {0}
{1, 0} is sorted to {0, 1}
{1, 0, 1, -1, 0} is sorted to {-1, 0, 0, 1, 1}
Assumptions

The input list is not null.
Corner Cases

What if the input list is of length zero? In this case, we should not do anything as well.
"""


class Solution(object):
    """
    解题思路：类似quick sort，只是需要分四个区域用三个挡板i, j, k => 把-1全移到left, 1全部移到右边，则中间是0
    three bounds:
    1. left side of neg is -1 (exclusive of neg)
    2. the right side of one is 1 （exclusive of one）
    3. the part between neg and zero is 0 (exclusive of zero)
    4. between zero and one is to be discovered (inclusive of both)
    Time: O(n)
    Space: O(1)
    """
    """
                            To Do: 必须结合九章的advanced Rainbow Sort, 进行总结
                            九章rainbowSort Review => similar to jiuzhang's Sort Color I
    """

    def rainbowSort(self, array):
        """
        input: int[] array
        return: int[]
        """
        # write your solution here
        # corner cases
        if array is None or len(array) <= 1:
            return array

        i, j = 0, 0;
        k = len(array) - 1

        while j <= k:
            if array[j] == -1:
                # swap j和i位置上的数如果i上的数不是-1，否则交换没意义
                if array[i] != -1:
                    array[i], array[j] = array[j], array[i]
                i += 1
                j += 1
            elif array[j] == 0:
                j += 1
            elif array[j] == 1:
                # 只有仅当交换位置k ！=1 的时候才需要交换，否则只是倒退k
                if array[k] != 1:
                    array[j], array[k] = array[k], array[j]
                k -= 1

        return array

print(Solution().rainbowSort([1,1,0,-1,0,1,-1]))  #[-1, -1, 0, 0, 1, 1, 1]