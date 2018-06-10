#
# Implement pow(x, n).
#
#
# Example 1:
#
# Input: 2.00000, 10
# Output: 1024.00000
# Example 2:
#
# Input: 2.10000, 3
# Output: 9.26100


### Solution 1
### normal math method to get result! not too fast
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        #         result = 1
        #         for i in range(n):
        #             result = result * x

        result = x ** n

        return result

### Solution 2
### normal brute force but time limit exceeded
### Time O(N), Space O(1)
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        result = 1
        for i in range(n):
            result = result * x


        return result


### Solution 3 二分法
### iterative method
### Time O(log(N)), Space O(1)
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        if n < 0:
            x = 1/x
            n = -n

        result = 1
        prod = x

        while n!= 0:
            if n % 2 == 1:
                result = result * prod
            prod = prod * prod
            n = n //2

        return result

# print(Solution().myPow(2,3)); #8
# print(Solution().myPow(2,-3)); #1/8
# print(Solution().myPow(2,2)); #4
# print(Solution().myPow(2,10)); #1024
# print(Solution().myPow(2,8)); #256

### Solution 3.2 二分法
### recursive method
### Time O(log(N)), Space O(log(N))
class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def myPow(self, x, n):
        if n==0:
            return 1
        if n<0:
            return 1.0/self.myPow(x,-n)
        if n%2==1:
            return x*self.myPow(x*x,n/2)
        else:
            return self.myPow(x*x,n/2)

print(Solution().myPow(2,3)); #8
print(Solution().myPow(2,-3)); #1/8
print(Solution().myPow(2,2)); #4
print(Solution().myPow(2,10)); #1024
print(Solution().myPow(2,8)); #256
