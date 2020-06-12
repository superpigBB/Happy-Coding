"""
Given two sequences pushed and popped with distinct values, return true if and only if this could
have been the result of a sequence of push and pop operations on an initially empty stack.

Example 1:

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
Example 2:

Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.

Note:
0 <= pushed.length == popped.length <= 1000
0 <= pushed[i], popped[i] < 1000
pushed is a permutation of popped.
pushed and popped have distinct values.
"""


class Solution(object):
    """解题思路： 借助第三个list(辅助栈)来模拟整个过程 =>存储element from pushed, 如果last element in new list == pop的index所在
                Value, 那就pop the value in new list =>如果最后new list为空，则代表成功
        Time: O(n)
        Spae: O(n)
    """
    def validateStackSequences(self, pushed, popped):
        """
        input: int[] pushed, int[] popped
        return: boolean
        """
        # write your solution here
        # write your solution here
        """Corner Cases"""
        if len(popped) != len(pushed):
            return False
        if len(pushed) == 0 and len(popped) == 0:
            return True

        help_stack = [];
        pop_index = 0
        for e in pushed:
            help_stack.append(e)
            while help_stack and help_stack[-1] == popped[pop_index]:
                help_stack.pop()
                pop_index += 1

        if len(help_stack) == 0:
            return True

        return False

