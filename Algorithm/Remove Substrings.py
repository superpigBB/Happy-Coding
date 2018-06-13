# Description
# Given a string s and a set of n substrings.
# You are supposed to remove every instance of those n substrings from s so that s is of the minimum length and output this minimum length.


# Example
# Given s = ccdaabcdbb, substrs = ["ab", "cd"]
# Return 2
#
# Explanation:
# ccdaabcdbb -> ccdacdbb -> cabb -> cb (length = 2)

## 这题难点就是在于要最小，想到所有情况，但直接想到是用BFS！
## 刚开始没想到BFS，但因为求最短s，因为去除substring的方法很多种，但要达到最短
## 就是要把各种solution都做出来，然后看哪个最短，有点像用BFS求最短路径的目的
## BFS：把原始string放入queue, 然后把缩减后的substring放入queue,看哪个最短
## Time:O(n + m) ,Space: O(n)
class Solution:
    """
    @param: s: a string
    @param: dict: a set of n substrings
    @return: the minimum length
    """

    def minLength(self, s, dict):
        # write your code here
        ## corner cases
        if s is None or len(s) == 0:
            return 0
        if dict is None or len(dict) == 0:
            return len(s)

        ## initialize queue/遍历过的路径set/minLen
        from collections import deque
        queue = deque([s])
        pathSet = set([s])
        minLen = len(s)

        while queue:
            s = queue.popleft()
            ## loop transformed neighbors of s by removing substrs in dict
            for substr in dict:
                index = s.find(substr)
                while index != - 1:
                    new_s = s[:index] + s[index + len(substr):]
                    if new_s not in pathSet:
                        pathSet.add(new_s)
                        queue.append(new_s)
                        ## compare length of new_s with minLen
                        if len(new_s) < minLen:
                            minLen = len(new_s)

                    index = s.find(substr, index + len(substr))
        return minLen



