"""
思路过程：
每一次循环当前数的所有int，比如10，for 2..10
一旦找到% x == 0 (x 不能是1和自己), 新的数 = n / x eg.10  / 2 = 5
5:
2 .. 4 -> 如果循环后发现没一个满足，则退出循环return factorized list

eg. 660: 2 .. 659
=> 2: 330 -> 330
             => 2: 165 -> 165: 2..164
                          => 3 : 55 -> 55: 2..54
                                       => 5: 11 -> 11
                                                   => 找不到 -> return

所以最差情况可能是每次都是2， 则Time: O(sqrt(n)), Space: O(log(n))
"""

class Solution:
    """
    @param num: An integer
    @return: an integer array
    """
    """
    正确方法：只循环有限次，设置up, up = sqrt(n) 
    超过这个up, k不可能被除自己以外的数整除
    Time: O(sqrt(n)) => 性能好
    """
    def primeFactorization(self, num):
    # write your code here
    ## Corner cases
        if num == 1:
            return []

        import math
        factor_list = []
        for i in range(2, int(math.sqrt(num)) + 1):
            # 如果能整除
            while num % i == 0:
                num = num // i
                factor_list.append(i)

        # 把剩余的没factor的数append
        if num != 1:
            factor_list.append(num)

        return factor_list

    """
    Time Limit Exceeded 错误方法： 循环长度N直到找不到除1的factor ，

    Time: O(n) => Exceeded time limit
    """
    def primeFactorization1(self, num):
        # write your code here
        ## Corner cases
        if num == 1:
            return []

        factor_list = []
        for i in range(2, num + 1):
            # 如果能整除
            while num % i == 0:
                num = num // i
                factor_list.append(i)


        return factor_list
