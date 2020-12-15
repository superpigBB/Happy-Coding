"""
Implement a recursive, pre-order traversal of a given binary tree,
return the list of keys of each node in the tree as it is pre-order traversed.

Examples

        5

      /    \

    3        8

  /   \        \

1      4        11

Pre-order traversal is [5, 3, 1, 4, 8, 11]

Corner Cases

What if the given binary tree is null? Return an empty list in this case.
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
    解题思路： 由上到下再由下至上的recursion
    Time: O(n)
    Space: O(h)
    """

    def preOrder(self, root):
        """
        input: TreeNode root
        return: Integer[]
        """
        # write your solution here
        result_list = list()
        self.traverse(root, result_list)
        return result_list

    def traverse(self, root, result_list):
        # base case
        if root is None:
            return

        result_list.append(root.val)
        self.traverse(root.left, result_list)
        self.traverse(root.right, result_list)
