"""
Enhance the stack implementation to support min() operation. min() should return the current minimum value in the stack.
If the stack is empty, min() should return -1.

push(int element) - push the element to top
pop() - return the top element and remove it, if the stack is empty, return -1
top() - return the top element without remove it, if the stack is empty, return -1
min() - return the current min value in the stack.
"""


class Solution(object):
    """
    解题思路：关键在于如何知道每次push,pop之后的每个节点的min value， 所以需要新建一个helper stack去保存每次操作Push,pop之后的min val
    Time: O(1)
    Space: O(n)
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []  # helper_stack => store min value of each operation

    def push(self, x):
        """
        input : int x
        return :
        """
        self.stack.append(x)
        # compare input value and min value in helper stack
        if not self.min_stack:  # if min_stack is empty
            self.min_stack.append(x)
        else:
            self.min_stack.append(min(self.min_stack[-1], x))
        '''the following statements are optional way to express'''
        # elif self.min_stack[-1] < x:   # if min stack栈顶值 < input
        #     self.min_stack.append(self.min_stack[-1])
        # else:      # if min stack栈顶值 >= input => append input as 栈顶
        #     self.min_stack.append(x)

    def pop(self):
        """
        return : int
        """
        if len(self.stack) == 0:
            return -1

        top_val = self.stack[-1]
        self.stack = self.stack[:-1]
        self.min_stack = self.min_stack[:-1]
        return top_val

    def top(self):
        """
        return : int
        """
        if len(self.stack) == 0:
            return -1
        return self.stack[-1]

    def min(self):
        """
        return : int
        """
        if len(self.stack) == 0:
          return -1
        return self.min_stack[-1]