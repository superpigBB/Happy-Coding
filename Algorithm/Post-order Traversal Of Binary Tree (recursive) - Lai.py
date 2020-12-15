"""
Implement a recursive, post-order traversal of a given binary tree,
return the list of keys of each node in the tree as it is post-order traversed.

Examples

        5

      /    \

    3        8

  /   \        \

1      4        11

Post-order traversal is [1, 4, 3, 11, 8, 5]

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
    解题思路：基本recursion
    Time: O(n)
    Space: O(h)
    """
    def postOrder(self, root):
        """
        input: TreeNode root
        return: Integer[]
        """
        # write your solution here
        # base case: root
        result_list = list()
        # need helper function
        self.traversal(root, result_list)
        return result_list

    def traversal(self, root, result_list):
        # base case: root
        if root is None:
            return

            # for left and right nodes
        if root.left:
            self.traversal(root.left, result_list)
        if root.right:
            self.traversal(root.right, result_list)
        if root:
            result_list.append(root.val)
