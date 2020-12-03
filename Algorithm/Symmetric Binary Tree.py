"""
Check if a given binary tree is symmetric.

Examples

        5

      /    \

    3        3

  /   \    /   \

1      4  4      1

is symmetric.

        5

      /    \

    3        3

  /   \    /   \

1      4  1      4

is not symmetric.

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
    解题思路：自上而下 => recursion left.left = right.right & left.right = right.left
    Time: O(n)
    Space: O(h)
    """

    def isSymmetric(self, root):
        """
        input: TreeNode root
        return: boolean
        """
        # write your solution here
        # base case: root
        if root is None:
            return True

            # left and right node=> might need a helper function for left node and right node
        return self.lrSymmetric(root.left, root.right)

    def lrSymmetric(self, left_node, right_node):
        # base cases
        if left_node is None and right_node is None:
            return True
        if (left_node and not right_node) or (not left_node and right_node):
            return False
            # left node is not None and right node is not None => compare values
        elif left_node.val != right_node.val:
            return False

        return self.lrSymmetric(left_node.left, right_node.right) and self.lrSymmetric(left_node.right, right_node.left)
