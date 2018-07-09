# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function
# to find the number of connected components in an undirected graph.
#
# Example 1:
#
# Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]
#
#      0          3
#      |          |
#      1 --- 2    4
#
# Output: 2
# Example 2:
#
# Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
#
#      0           4
#      |           |
#      1 --- 2 --- 3
#
# Output:  1
# Note:
# You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0]
# and thus will not appear together in edges.


## 这题和lintcode 431.connected-component-in-undirected-graph 属于一道题，就是问法不一样
## Solution 1) BFS/DFS ;  Solution 2) Union Find

## Solution 1):
## 先把edge list转变为adjacent list, 然后用BFS
## Time: O(N+ M), Space: O(n)
class Solution:
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # write your code here
        ## corner cases
        if n is None or n == 0:
            return 0

        ## 遍历edges得到每个node的adjacent list
        from collections import defaultdict
        nodeNeighbors = defaultdict(set)  # neighbors of each node => {node: set(neighbors)}

        for edge in edges:
            nodeNeighbors[edge[0]].add(edge[1])
            nodeNeighbors[edge[1]].add(edge[0])

        ## initialization
        visitedNodes = set()  # hashset to save visited nodes
        componentCnt = 0
        from collections import deque
        queue = deque([])

        ## loop all nodes
        # import heapq
        for node in range(n):
            if node in visitedNodes:
                continue
            visitedNodes.add(node)
            queue.append(node)
            ## loop queue until empty
            while queue:
                graphNode = queue.popleft()
                for neighbor in nodeNeighbors[graphNode]:
                    if neighbor not in visitedNodes:
                        visitedNodes.add(neighbor)
                        queue.append(neighbor)

            componentCnt += 1

        return componentCnt

