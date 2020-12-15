"""
Check if a given binary tree is balanced.
A balanced binary tree is one in which the depths of every node’s left and right subtree differ by at most 1.

Examples

        5

      /    \

    3        8

  /   \        \

1      4        11

is balanced binary tree,

        5

      /

    3

  /   \

1      4

is not balanced binary tree.

Corner Cases

What if the binary tree is null? Return true in this case.
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
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    """
    两种解法
    """
    """
    解题思路： 为了避免自顶向下多次调用的height function， 我们可以直接用自底向上的recursion，这样可以每个node只算
    一次height
    Time: O(n)
    Space: O(h)
    """
    def isBalanced1(self, root):
        """
        input: TreeNode root
        return: boolean
        """
        # write your solution here
        # if balanced then height should be returned as positive, but if any is unbalanced
        # then it will return -1
        return self.height_check(root) >= 0

    def height_check(self, root):
        # base cases
        if root is None:
            return 0

        # for left and right nodes:
        left_height = self.height_check(root.left)
        right_height = self.height_check(root.right)

        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            return -1

        # 如果balanced则返回实际height
        return max(left_height, right_height) + 1

    """
    解题思路： 自顶向下recursion 判断
    Time: O(n^2 最差情况， nlogn on average)
    Space: O(h)
    """
    def isBalanced2(self, root):
        """
        input: TreeNode root
        return: boolean
        """
        # write your solution here
        # base cases
        if root is None:
            return True

            # for left and right nodes
        if abs(self.height(root.left) - self.height(root.right)) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, root):
        # base cases
        if root is None:
            return 0

        # for left and right nodes
        left_height = self.height(root.left)
        right_height = self.height(root.right)

        return max(left_height, right_height) + 1