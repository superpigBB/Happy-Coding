"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example
Given binary tree {1,#,2,3},

   1
    \
     2
    /
   3


return [1,3,2].

Challenge
Can you do it without recursion?
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

"""
思路过程:
方法一： recursion ->比较简单
Time: O(N), Space: O(N)

方法二： iteration 
比较难直接用level traverse 也就是BFS的思想直接做
更类似于DFS的iteration 方法： 先把相关左子树的node都放在stack里，
然后一个个Pop,再找该node有没相应的右子树=>如果有，继续遍历右子树的左子树并放到stack
里，周而复始。。。
Time: O(N), Space: O(N)
"""


class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """

    """
    方法一： iteration 
    Time: O(N), Space: O(N)
    original: left -> root -> right 
    """

    def inorderTraversal(self, root):
        # write your code here
        ## corner cases
        if not root:
            return []

        ## 先把root和所有他的左子树放在stack里
        stack = [root]
        while root.left:
            stack.append(root.left)
            root = root.left
        """
        或这么写
        stack = []
        while root:
            stack.append(root)
            root = root.left
        """

        ## set up resultList并访问所有stack里node的右子树
        resultList = []
        while stack:
            node = stack.pop()
            resultList.append(node.val)

            ## 如果存在右子树
            if node.right:
                ##对右子树里的左子树进行遍历并加到stack里
                node = node.right
                stack.append(node)
                while node.left:
                    stack.append(node.left)
                    node = node.left
                """
                或这么写
                while node:
                    stack.append(node)
                    node = node.left 
                 """

        return resultList

    """
     方法二： recursion 
     Time: O(N), Space: O(N)
     original: left -> root -> right 
     """
    resultList = []

    def inorderTraversal(self, root):
        # write your code here
        self.resultList = []
        self.traverse(root)
        return self.resultList

    def traverse(self, node):
        if not node:
            return

        self.traverse(node.left)
        self.resultList.append(node.val)
        self.traverse(node.right)
