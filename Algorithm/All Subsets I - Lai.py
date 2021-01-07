"""
Given a set of characters represented by a String, return a list containing all subsets of the characters.

Assumptions

There are no duplicate characters in the original set.
​Examples

Set = "abc", all the subsets are [“”, “a”, “ab”, “abc”, “ac”, “b”, “bc”, “c”]
Set = "", all the subsets are [""]
Set = null, all the subsets are []
"""


class Solution(object):
    """"""
    """
    解题思路：这题是求组合的问题
    每一层代表： 层数fixed => 一共len(set)层，加set[index] or 不加
    每一层的states: fixed => 2个，select or not select
    Time: O(2^n * n), 其中*n代表复制时间复杂度
    Space: O(n), n = len(set)
    """

    def subSets(self, set):
        """
        input : String set
        return : String[]
        """
        # write your solution here
        # corner cases
        if set is None:
            return []
        if len(set) == 0:
            return [""]

        result = list()
        self.dfs(set, 0, [], result)
        return result

    def dfs(self, set, index, subset, result):
        # base cases
        if index == len(set):
            result.append(''.join(subset))
            return

        # select set[index]
        subset.append(set[index])
        # 往下递归
        self.dfs(set, index + 1, subset, result)
        # 到底后backtracking且unselect previous selection
        subset.pop()

        # unselect set[index]
        self.dfs(set, index + 1, subset, result)
