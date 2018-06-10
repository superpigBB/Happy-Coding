# There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you.
# You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language.
# Derive the order of letters in this language.
#
# Example 1:
# Given the following words in dictionary,
#
# [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]
# The correct order is: "wertf".
#
# Example 2:
# Given the following words in dictionary,
#
# [
#   "z",
#   "x"
# ]
# The correct order is: "zx".
#
# Example 3:
# Given the following words in dictionary,
#
# [
#   "z",
#   "x",
#   "z"
# ]
# The order is invalid, so return "".
#
# Note:
# You may assume all letters are in lowercase.
# You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
# If the order is invalid, return an empty string.
# There may be multiple valid order of letters, return any one of them is fine.



## Solution 1: 用list存graph =》 Solution 1.1 用dict存graph =》 Solution 1.2用defaultdict存graph
## Solution 1.1 and 1.2还会用到zip，只是为了熟练掌握下zip
## 看下Performance能否得到提高
## 这种题涉及到了有向性，先后性，还有最后问order,应该要想到是topology sorting order
## BFS topology
## 因为要求对同层order的node要求返回lexicographical order,所以可以用heapq module in python=》PriorityQueue
class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """

    def alienOrder(self, words):
        # Write your code here
        nodes = []  ## distinct letter in a list of words
        for word in words:
            for letter in word:
                if letter not in nodes:
                    nodes.append(letter)
        print("nodes: ", nodes)

        ## initialize neighbors of each node: adjacent list
        nodes_neighbors = [[] for i in range(len(nodes))]
        ##纵向对比直到发现不一样，然后那个i+1行不一样的就是i行的那个的neighbor
        for i in range(len(words) - 1):
            j = 0  ## column index
            while j < len(words[i]) and j < len(words[i + 1]):
                if words[i][j] != words[i + 1][j]:
                    IndexofNode = nodes.index(words[i][j])
                    nodes_neighbors[IndexofNode].append(words[i + 1][j])
                    break
                j += 1
        print("neighbors of nodes: ", nodes_neighbors)

        ## count indegree using hash
        node_indegree = {}
        for neighbor_list in nodes_neighbors:
            for letter in neighbor_list:
                if letter not in node_indegree:
                    node_indegree[letter] = 1
                else:
                    node_indegree[letter] += 1

        ## store those indegree = 0 node into top_str and Priority Queue
        from heapq import heappush, heappop
        top_str = ''
        heap_queue = []

        for node in nodes:
            if node not in node_indegree:
                heappush(heap_queue, node)

        ## topological sorting
        while heap_queue:
            node = heappop(heap_queue)
            top_str += node
            IndexofNode = nodes.index(node)  ## to find corresponding neighbors in nodes_neighbors
            for neighbor in nodes_neighbors[IndexofNode]:
                node_indegree[neighbor] -= 1
                if node_indegree[neighbor] == 0:
                    heappush(heap_queue, neighbor)

        print("topological string is ", top_str)
        ## judge whether it's topological sorting
        if len(top_str) == len(nodes):
            return top_str

        else:
            return ''















