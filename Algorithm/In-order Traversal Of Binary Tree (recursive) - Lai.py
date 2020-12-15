"""
Implement a recursive, in-order traversal of a given binary tree, return the list of keys of each node in the tree as it is in-order traversed.

Examples

        5

      /    \

    3        8

  /   \        \

1      4        11

In-order traversal is [1, 3, 4, 5, 8, 11]

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
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    """
    解题思路： 基本的traversal
    Time: O(n)
    Space: O(h)
    """
    def inOrder(self, root):
        """Î
        input: TreeNode root
        return: Integer[]
        """
        # write your solution here
        # root itself
        return_list = list()
        self.traverse(root, return_list)
        return return_list

    def traverse(self, root, list):
        # base root
        if root is None:
            return

        # left and right child
        self.traverse(root.left, list)
        list.append(root.val)
        self.traverse(root.right, list)


n1 = TreeNode(2); n2 = TreeNode(1); n3 = TreeNode(3)
n1.left = n2; n1.right = n3

print(Solution().inOrder(n1))

