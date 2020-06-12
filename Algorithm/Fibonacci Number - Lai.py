"""
Get the Kth number in the Fibonacci Sequence.
(K is 0-indexed, the 0th Fibonacci number is 0 and the 1st Fibonacci number is 1).

Examples

0th fibonacci number is 0
1st fibonacci number is 1
2nd fibonacci number is 1
3rd fibonacci number is 2
6th fibonacci number is 8
Corner Cases

What if K < 0? in this case, we should always return 0.
Is it possible the result fibonacci number is overflowed?
We can assume it will not be overflowed when we solve this problem on this online judge,
but we should also know that it is possible to get an overflowed number,
and sometimes we will need to use something like BigInteger.
"""


class Solution(object):
    """"
    解题思路： 就是一道recursion基本练习题来理解recursion=> f(k) = f(k-1) + f(k-2)
    时间复杂度和空间复杂度分析是重点！
    Time: O(2^k)
    Space: O(k)
    """
    def fibonacci(self, K):
        """
        input: int K
        return: long
        """
        # write your solution here
        """ Corner Cases """
        if K <= 0:
            return 0
        if K == 1:
            return 1

        return self.fibonacci(K-1) + self.fibonacci(K-2)


print(Solution().fibonacci(6))



