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
    def rainbowSort(self, list):
        """
        input: int[] list
        return: int[]
        """
        # write your solution here
        """Corner Cases"""
        if list is None or len(list) == 0 or len(list) == 1:
            return list

        left = 0; right = len(list) - 1
        index = 0
        while index <= right:
            if list[index] == -1:
                list[index], list[left] = list[left], list[index]
                left += 1
                index += 1
            elif list[index] == 1:
                list[index], list[right] = list[right], list[index]
                right -= 1
            else:
                index += 1

        return list

print(Solution().rainbowSort([1,1,0,-1,0,1,-1]))  #[-1, -1, 0, 0, 1, 1, 1]