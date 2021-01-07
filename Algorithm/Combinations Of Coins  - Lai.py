"""
Given a number of different denominations of coins (e.g., 1 cent, 5 cents, 10 cents, 25 cents),
get all the possible ways to pay a target number of cents.

Arguments

coins - an array of positive integers representing the different denominations of coins,
there are no duplicate numbers and the numbers are sorted by descending order, eg. {25, 10, 5, 2, 1}
target - a non-negative integer representing the target number of cents, eg. 99
Assumptions

coins is not null and is not empty, all the numbers in coins are positive
target >= 0
You have infinite number of coins for each of the denominations, you can pick any number of the coins.
Return

a list of ways of combinations of coins to sum up to be target.
each way of combinations is represented by list of integer, the number at each index means the number of coins
used for the denomination at corresponding index.
Examples

coins = {2, 1}, target = 4, the return should be

[

  [0, 4],   (4 cents can be conducted by 0 * 2 cents + 4 * 1 cents)

  [1, 2],   (4 cents can be conducted by 1 * 2 cents + 2 * 1 cents)

  [2, 0]    (4 cents can be conducted by 2 * 2 cents + 0 * 1 cents)

]

"""


class Solution(object):
    """"""
    """
    解题思路： 还是组合题，用DFS
    每一层代表： combination里每一个cent， 一共len(coins) n 层
    每一层states: dynamic个数， 取决于target // coins[index] 
    Time: O(max(target // coins[index]) ^ n)
    Space: O(n)
    """

    """
    第一种方法：比较直接和模板化，直接遍历每一层直到index = len(coins),我现在比较喜欢
    """
    def combinations(self, target, coins):
        """
        input: int target, int[] coins
        return: int[][]
        """
        # write your solution here
        # corner cases
        if target == 0 or coins is None:
            return [[]]

        result = list()
        self.dfs(coins, 0, target, [], result)
        return result

    def dfs(self, coins, index, target, solu, result):
        # base cases
        if target < 0:
            return
        if index == len(coins):
            if target == 0:
                result.append(solu[:])
            return

        # 对每一层states loop
        for num in range(target // coins[index] + 1):
            solu.append(num)
            # 往下走
            self.dfs(coins, index + 1, target - num * coins[index], solu, result)
            # 还原
            solu.pop()

    """
    第二种方法： 比较巧妙，不需要走到最后一层浪费时间，可以到len(coin - 1)层直接检查数值是不是能被剩余target整除
    """

    def dfs2(self, target, coins, coin_index, combo, result):
        # base cases
        # this method is to reduce some unnecessary branches and do dfs until n - 1 level
        if coin_index == len(coins) - 1:
            if target % coins[len(coins) - 1] == 0:
                combo.append(target // coins[len(coins) - 1])
                result.append(combo[:])
                combo.pop()
            return
        if target < 0:
            return

        for i in range(target // coins[coin_index] + 1):
            combo.append(i)
            self.dfs(target - i * coins[coin_index], coins, coin_index + 1, combo, result)
            combo.pop()
