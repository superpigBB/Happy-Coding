# Implement the following operations of a queue using stacks.
#
# push(x) -- Push element x to the back of queue.
# pop() -- Removes the element from in front of queue.
# peek() -- Get the front element.
# empty() -- Return whether the queue is empty.
# Notes:
# You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
# You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).

### Solution 1
### 双栈 O(1) in average in time and O(N) in space

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack1.append(x)

    def stack1tostack2(self):
        if len(self.stack2) == 0:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.stack1tostack2()
        return self.stack2.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        self.stack1tostack2()
        return self.stack2[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        self.stack1tostack2()
        return len(self.stack2) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

### Solution 2： from online solution
### 单栈 O(1) in average in time but push use O(N) and O(N) in space

class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.stack = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        swap = []
        while self.stack:
            swap.append(self.stack.pop())
        swap.append(x)
        while swap:
            self.stack.append(swap.pop())

    # @return nothing
    def pop(self):
        self.stack.pop()

    # @return an integer
    def peek(self):
        return self.stack[-1]

    # @return an boolean
    def empty(self):
        return len(self.stack) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()