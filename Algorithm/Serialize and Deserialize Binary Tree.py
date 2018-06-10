### LeetCode Version

#########################################################################################

# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer,
#
# or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
#
# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm
# should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized
# to the original tree structure.
#
# Example:
#
# You may serialize the following tree:
#
#     1
#    / \
#   2   3
#      / \
#     4   5
#
# as "[1,2,3,null,null,4,5]"
# Clarification: Just the same as how LeetCode OJ serializes a binary tree. You do not necessarily need to follow this format, so please be
# creative and come up with different approaches yourself.
#
# Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

## BFS 遍历 做serialize and deserialie
class Codec:

    ## 先把相关node value存到list里，然后再把list转换为string,因为string是immutable,比较费时间/空间
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        ## corner cases
        if root is None:
            return '[]'

        ## initialize queue to stort BFS
        from collections import deque
        queue = deque([root])
        ## initialize list to store nodes
        result = [root.val]

        while queue:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            result.append(node.left.val if node.left else 'null')
            result.append(node.right.val if node.right else 'null')

        ## remove extra 'null's at the end of list
        while result and result[-1] == 'null':
            result.pop()

        ## transform list to string
        # return '[' + ','.join(map(str, result)) + ']'
        return '[%s]' % ','.join(str(val) if type(val) == int else 'null' for val in result)

    ## use BFS to return root
    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        ## corner cases
        if data == '[]':
            return None

        ## transform data into list and clean up data list with numbers and nulls only
        from collections import deque
        result = deque([TreeNode(val) if val != 'null' else None for val in data[1:-1].split(',')])
        root = result.popleft()## get root node
        queue = deque([root])

        while queue:
            parent = queue.popleft()
            leftnode = result.popleft() if result else None
            rightnode = result.popleft() if result else None

            if leftnode:
                queue.append(leftnode)
            if rightnode:
                queue.append(rightnode)

            ## 左子树右子树连接
            parent.left = leftnode
            parent.right = rightnode

        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))