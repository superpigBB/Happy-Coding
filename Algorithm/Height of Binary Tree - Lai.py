"""
Find the height of binary tree.

Examples:

        5

      /    \

    3        8

  /   \        \

1      4        11

The height of above binary tree is 3.

How is the binary tree represented?

We use the level order traversal sequence with a special symbol "#" denoting the null node.

For Example:

The sequence [1, 2, 3, #, #, 4] represents the following binary tree:

    1

  /   \

 2     3

      /

    4

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    """
    解题思路： recursion
    Time： O(n)
    Space： O（h）
    """

    def findHeight(self, root):
        """
        input: TreeNode root
        return: int
        """
        # write your solution here
        # base case: root only
        if root is None:
            return 0

        # left and right node
        left_height = self.findHeight(root.left)
        right_height = self.findHeight(root.right)

        # Tree Height
        return max(left_height, right_height) + 1