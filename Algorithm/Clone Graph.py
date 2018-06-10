# Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.
#
#
# OJ's undirected graph serialization:
# Nodes are labeled uniquely.
#
# We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
# As an example, consider the serialized graph {0,1,2#1,2#2,2}.
#
# The graph has a total of three nodes, and therefore contains three parts as separated by #.
#
# First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
# Second node is labeled as 1. Connect node 1 to node 2.
# Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
# Visually, the graph looks like the following:
#
#        1
#       / \
#      /   \
#     0 --- 2
#          / \
#          \_/

"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

## Solution 1: only solution: 能拆就拆， 容易debug!!!
## 由点及面=》BFS
## 根据给的一个node，要找出所有neighbors还有lines，用BFS算出这个图
## 然后用hash以原node为key, 复制的node为value遍历所有原图上的点
## 根据原图的line的连线，把复制的点连线也都弄好
class Solution:
    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """

    def cloneGraph(self, node):
        # write your code here
        ## 先存这个node,因为后面运行也用node这个名字，值容易被替换
        root = node
        ## corner cases
        if node is None:
            return node

        ##通过BFS找出所有点
        from collections import deque
        queue = deque([node])
        all_nodes = {node}  ## set

        while queue:
            node = queue.popleft()
            for neighbor in set(node.neighbors):
                if neighbor not in all_nodes:
                    queue.append(neighbor)
                    all_nodes.add(neighbor)

        ## clone nodes
        from collections import defaultdict
        node_dict = defaultdict()          ## or 直接node_dict = {} 在数据量不大适合{}更快

        for node in all_nodes:
            node_dict[node] = UndirectedGraphNode(node.label)

        ## clone connected lines: neighbors
        for node in all_nodes:
            new_node = node_dict[node]
            for neighbor in node.neighbors:
                new_neighbor = node_dict[neighbor]
                new_node.neighbors.append(new_neighbor)

        return node_dict[root]

