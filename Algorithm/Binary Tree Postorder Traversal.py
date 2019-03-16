"""
Given a binary tree, return the postorder traversal of its nodes' values.

Example
Given binary tree {1,#,2,3},

   1
    \
     2
    /
   3


return [3,2,1].

Challenge
Can you do it without recursion?

Notice
The first data is the root node, followed by the value of the left and right son nodes, and "#" indicates that there is
no child node.
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

"""
思路过程：
postorder: left -> right -> root
方法一： 如果是recursion, Time: O(N), Space: O(N)

方法二： iteration
因为是后续遍历，要从1，2，3 -> 3, 2 ,1 
类似先进后出， 可能要用到stack的知识 =》改变原先顺序以逆顺序 root -> right -> left并把每个遍历的root val保存的一个List，最后pop这些value 到result list 
Time: O(N), Space: O(2N)
"""

class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    """
    方法一： 遍历recursion 
    Time: O(N), Space: O(N)
    """
    def postorderTraversal(self, root):
        # write your code here
        resultList = []
        self.traverse(root, resultList)
        return resultList

    def traverse(self, root, l):
        if not root:
            return

        self.traverse(root.left, l)
        self.traverse(root.right, l)
        l.append(root.val)

    """
    Or make resultList a global variable using self.resultList
    """
    resultList = []
    def postorderTraversal(self, root):
        # write your code here
        self.resultList = []
        self.traverse(root)
        return self.resultList

    def traverse(self, root):
        if not root:
            return

        self.traverse(root.left)
        self.traverse(root.right)
        self.resultList.append(root.val)

    """
    方法二：iteration 遍历，利用两个stack 
    遍历root->right->left 得到一个new list
    pop new list -> result list 
    Time: O(N), Space: O(N)
    """
    def postorderTraversal(self, root):
        ## corner cases
        if not root:
            return []

        ## initialization
        traverseList = [root]
        resultList = []


        while traverseList:
            node = traverseList.pop()
            resultList.append(node.val)

            if node.left is not None:
                traverseList.append(node.left)
            if node.right is not None:
                traverseList.append(node.right)

        return resultList[::-1]


