class Solution(object):
    """
    Time: O(1)
    Space: O(n)
    """

    def __init__(self):
        self.stack = []
        self.min_stack = []  # store min value of each operation

    def push(self, x):
        self.stack.append(x)
        # compare input value and min value in helper stack
        if not self.min_stack:  # if min_stack is empty
            self.min_stack.append(x)
        else:
            self.min_stack.append(min(self.min_stack[-1], x))

    def pop(self):
        if len(self.stack) == 0:
            return -1

        top_val = self.stack[-1]
        self.stack = self.stack[:-1]
        self.min_stack = self.min_stack[:-1]
        return top_val

    def top(self):
        if len(self.stack) == 0:
            return -1
        return self.stack[-1]

    def getMin(self):
        if len(self.stack) == 0:
          return -1
        return self.min_stack[-1]