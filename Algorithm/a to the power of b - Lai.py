"""
Evaluate a to the power of b, assuming both a and b are integers and b is non-negative.

Examples

power(2, 0) = 1
power(2, 3) = 8
power(0, 10) = 0
power(-2, 5) = -32
Corner Cases

In this question, we assume 0^0 = 1.
What if the result is overflowed? We can assume the result will not be overflowed when we solve this problem
on this online judge.
"""


class Solution(object):
    """
    解题思路： 传统recursion的分治思想就可以做; 如果用传统方法，容易空间复杂度很高a^b = a^b-1 * a = a^b-2 * a * a, ...
    所以可以考虑把b分成 b //2 以及b - b//2 这样空间就相对相等划分节省了space complexity; 但因为左右两边计算一样，这样又额外费了
    time complexity;
    所以最好的方法就是把b分成奇数和偶数考虑，同样也是b//2的解法，如果是奇数，那就是单边 * 底数；如果是偶数，直接算单边Time complexity
    Time: O(logb)
    Space: O(logb)
    """
    def power(self, a, b):
        """
        input: int a, int b
        return: long
        """
        # write your solution here
        """base case"""
        if b == 0:
            return 1
        if b == 1:
            return a

        # b is even number
        if b % 2 == 0:
            return self.power(a, b // 2) ** 2
        # b is odd number
        else:
            return self.power(a, (b - 1) // 2) **2 * a
