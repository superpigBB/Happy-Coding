#
# Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs. The org sequence is a permutation of the integers from 1 to n, with 1 ≤ n ≤ 104. Reconstruction means building a shortest common supersequence of the sequences in seqs (i.e., a shortest sequence so that all sequences in seqs are subsequences of it). Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.
#
# Example 1:
#
# Input:
# org: [1,2,3], seqs: [[1,2],[1,3]]
#
# Output:
# false
#
# Explanation:
# [1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.
# Example 2:
#
# Input:
# org: [1,2,3], seqs: [[1,2]]
#
# Output:
# false
#
# Explanation:
# The reconstructed sequence can only be [1,2].
# Example 3:
#
# Input:
# org: [1,2,3], seqs: [[1,2],[1,3],[2,3]]
#
# Output:
# true
#
# Explanation:
# The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].
# Example 4:
#
# Input:
# org: [4,1,5,2,6,3], seqs: [[5,2,6,3],[4,1,5,2]]
#
# Output:
# true


## Solution1: BFS + Topology， 和Solution 2唯一区别就在于exceptions的排除判断
## 这题是针对seqs的构图和入度求topological sorting list
## 而且有且仅有一条 =》 就要求每一层的level size都是1
## BFS topology 做
## neighbor table: hashmap: hashset
## Time:  Space:
class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """

    def sequenceReconstruction(self, org, seqs):
        # write your code here
        ## exceptions
        if len(seqs) == 0 or all(len(l) == 0 and len(org) != 0 for l in seqs):
            return False

        seqs_set = set(e for l in seqs for e in l)
        if seqs_set != set(org):
            return False

        from collections import defaultdict
        ## initialize hashmap with value: hashset to save neighbors of each node
        SeqNeighbors = defaultdict(set)
        ## initialize indegree hash with integers
        SeqIndegree = defaultdict(int)

        ## Loop Seqs 来得到SeqNeighbors和SeqIndegree
        for l in seqs:
            for i in range(len(l) - 1):
                ## prevent same values set added into SeqNeighbors and SeqIndegree, eg. [1, 5], [1, 5]
                if l[i + 1] not in SeqNeighbors[l[i]]:
                    SeqNeighbors[l[i]].add(l[i + 1])
                    SeqIndegree[l[i + 1]] += 1

        # print (SeqNeighbors)
        # print (SeqIndegree)
        ## initialize topology list and BFS queue
        from collections import deque
        top_list = []
        queue = deque([])

        ## find those indegree = 0 to top_list and first level of queue
        for seq in org:
            if seq not in SeqIndegree:
                top_list.append(seq)
                queue.append(seq)

        ## loop queue
        while queue:
            ## 判断每层的seq个数是不是超过1，超过1就不唯一
            if len(queue) > 1:
                return False

            ## 如果不超过1, append到top_list看是否等于org
            seq = queue.popleft()
            ## loop neighbors of seq
            for neighbor in SeqNeighbors[seq]:
                SeqIndegree[neighbor] -= 1
                if SeqIndegree[neighbor] == 0:
                    top_list.append(neighbor)
                    queue.append(neighbor)

        # print(top_list)
        ## 判断是否top_list == org
        return top_list == org


## Solution2
## 这题是针对seqs的构图和入度求topological sorting list
## 而且有且仅有一条 =》 就要求每一层的level size都是1
## BFS topology 做
## neighbor table: hashmap: hashset
## Time:  Space:
class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """

    def sequenceReconstruction(self, org, seqs):
        # write your code here

        from collections import defaultdict
        ## initialize hashmap with value: hashset to save neighbors of each node
        SeqNeighbors = defaultdict(set)
        ## initialize indegree hash with integers
        SeqIndegree = defaultdict(int)

        seq_cnt = 0
        ## Loop Seqs 来得到SeqNeighbors和SeqIndegree
        for l in seqs:
            ## exceptions for case [1], [[]]
            seq_cnt += len(l)

            for i in range(len(l) - 1):
                ## exceptions for element beyond or below boundaries of org
                ## case [1,2,3] [[1,2,3], [5]]
                if (l[i] < 1 or l[i] > len(org)):
                    return False
                ## prevent same values set added into SeqNeighbors and SeqIndegree, eg. [1, 5], [1, 5]
                if l[i + 1] not in SeqNeighbors[l[i]]:
                    SeqNeighbors[l[i]].add(l[i + 1])
                    SeqIndegree[l[i + 1]] += 1
            ## exceptions for last element of l [1], [[1], [5]]
            if len(l) > 0 and (l[-1] < 1 or l[-1] > len(org)):
                return False

        ## exceptions for case [1], [[]]
        if seq_cnt < len(org):
            return False

        # print (SeqNeighbors)
        # print (SeqIndegree)
        ## initialize topology list and BFS queue
        from collections import deque
        top_list = []
        queue = deque([])

        ## find those indegree = 0 to top_list and first level of queue
        for seq in org:
            if seq not in SeqIndegree:
                top_list.append(seq)
                queue.append(seq)

        ## loop queue
        while queue:
            ## 判断每层的seq个数是不是超过1，超过1就不唯一
            if len(queue) > 1:
                return False

            ## 如果不超过1, append到top_list看是否等于org
            seq = queue.popleft()
            ## loop neighbors of seq
            for neighbor in SeqNeighbors[seq]:
                SeqIndegree[neighbor] -= 1
                if SeqIndegree[neighbor] == 0:
                    top_list.append(neighbor)
                    queue.append(neighbor)

        # print(top_list)
        ## 判断是否top_list == org
        return top_list == org
