"""
Given a string with no duplicate characters, return a list with all permutations of the characters.

Assume that input string is not null.

Examples

Set = “abc”, all permutations are [“abc”, “acb”, “bac”, “bca”, “cab”, “cba”]

Set = "", all permutations are [""]
"""


class Solution(object):
    """"""
    """
    解题思路：排列题用DFS，而且这题是最后排列结果里的subsets里所有元素都是由原来input里的char组成，可以考虑用swap方法
    每一层代表： pos, 一共len(input)层
    每一层states: 除了第一个char以外的所有chars
    Time: O(n! * n)
    Space: O(n)
    """

    def permutations(self, input):
        """
        input: string input
        return: string[]
        """
        # write your solution here
        # corner cases
        if input is None:
            return []
        if len(input) == 0:
            return [""]

        result = list()
        # 因为string immutable, 而且过程中要swap， better to be list instead string
        inputs = [char for char in input]
        self.dfs(inputs, 0, result)
        return result

    def dfs(self, inputs, pos, result):
        # base cases
        if len(inputs) == pos:
            result.append(''.join(inputs))
            return

            # for loop 在对每一层里每一个states是什么情况
        for i in range(pos, len(inputs)):
            # swap
            inputs[pos], inputs[i] = inputs[i], inputs[pos]
            # 进入下一层
            self.dfs(inputs, pos + 1, result)
            # 触底后swap回来
            inputs[pos], inputs[i] = inputs[i], inputs[pos]

