class Solution(object):
    """
    解题思路： 组合题，但需要剪枝 => DFS做
    每一层代表： + （ or + ）， 一共2n层
    每一层states: 2, select ( or select )
    Time: 第n个卡特兰数 (2^2n/(n*sqrt(n)) * n) => 4^n/sqrt(n)
    Space: O(n)
    """

    def validParentheses(self, n):
        """
        input: int n
        return: string[]
        """
        # write your solution here
        # corner cases
        if n == 0:
            return []

        result = list()
        self.dfs(n, 0, 0, [], result)
        return result

    def dfs(self, n, left, right, subset, result):
        # base cases
        if left == n and right == n:  # or len(subset) == 2 * n
            result.append(''.join(subset[:]))
            return

            # select (
            if left < n:
                subset.append('(')
                self.dfs(n, left + 1, right, subset, result)
                # unselect
                subset.pop()

            if right < left:
                subset.append(')')
                self.dfs(n, left, right + 1, subset, result)
                subset.pop()

print(Solution().validParentheses(6))