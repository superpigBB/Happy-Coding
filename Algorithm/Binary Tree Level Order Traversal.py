# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
#
# return its level order traversal as:
#
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


### Solution1： BFS 新建result 和 level array，使用单数列
### Time O(N), Space O(N)
class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """

    def levelOrder(self, root):
        # write your code here
        ## 异常值检测
        if root is None:
            return []

        ## initialize array to store list of levels
        result = []
        ## add root node into queue
        from collections import deque
        q = deque([root])

        while q:
            ## initialize array to store levels of nodes
            level = []
            ## traverse level by level
            size = len(q)
            for i in range(size):
                head = q.popleft()
                level.append(head.val)
                if head.left is not None:
                    q.append(head.left)
                if head.right is not None:
                    q.append(head.right)

            result.append(level)

        return result


###Solution 2： 使用两个队列的BFS
class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """

    def levelOrder(self, root):
        # write your code here
        ## 异常值检测
        if root is None:
            return []

        ## initialize array to store list of levels
        result = []
        ## add root node into queue1
        from collections import deque
        q1 = deque([root])
        q2 = deque([])

        while q1:
            ## initialize array to store levels of nodes
            level = []
            ## traverse queue 1 and store child nodes into queue 2
            for i in range(len(q1)):
                head = q1.popleft
                level.append(head.val)
                if head.left is not None:
                    q2.append(head.left)
                if head.right is not None:
                    q2.append(head.right)
            ## exchange q1 and q2: after loop, q1 should be empty
            q1, q2 = q2, q1
            result.append(level)

        return result

### Solution 3: DFS