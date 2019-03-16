"""
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""
"""
方法一： Iteration 
因为pre-order是root->left->right, 所以用stack顺序是root->right->left
Time: O(N) Space:O(N) 

方法二： recursion
Time: O(N), Space: O(N)
"""


class Solution(object):
    """
    方法一： iteration
    """

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        ## corner cases
        if not root:
            return []

        ## initialization
        traverseList = [root]
        resultList = []

        while traverseList:
            node = traverseList.pop()
            resultList.append(node.val)

            if node.right is not None:
                traverseList.append(node.right)
            if node.left is not None:
                traverseList.append(node.left)

        return resultList

    """
    方法二： recursion
    """

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        resultList = []
        self.traverse(root, resultList)
        return resultList

    def traverse(self, root, l):
        if not root:
            return

        l.append(root.val)
        self.traverse(root.left, l)
        self.traverse(root.right, l)