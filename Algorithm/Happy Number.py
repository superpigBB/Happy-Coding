# Write an algorithm to determine if a number is "happy".
#
# A happy number is a number defined by the following process: Starting with any positive integer,
# replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay),
# or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
#
# Example: 19 is a happy number
#
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1

### Solution 1
### Time O(nlogn), space O(1)

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sum = 0
        dict = {}
        while sum != 1:
            sum = 0
            while n != 0:
                a = n % 10
                # print("a is %d" %a)
                sum += a **2
                # print ('sum is %d' %sum)
                n = n // 10
                # print("n is %d" %n)
            # print ("after loop sum is %d" %sum)

            if sum != 1:

                if sum in dict:
                    return False
                else:
                    n = sum
                dict[sum] = 1

        return sum == 1

# print(Solution().isHappy(19))     # True
# print(Solution().isHappy(10))     # True
# print(Solution().isHappy(1))      # True
# print(Solution().isHappy(2))      # False
# print('\n')

### Solution 2: more concise, using list comprehensive, instead of using % /, it utilize the characteristics of string
### copy from jiuzhang time and space complexity should be the same
class Solution:
    # @param {int} n an integer
    # @return {boolean} true if this is a happy number or false
    def isHappy(self, n):
        # Write your code here
        d = {}
        while True:
            d[n] = 1
            n = sum([int(x) * int(x) for x in list(str(n))])
            if n == 1 or n in d:
                break
        return n == 1

print(Solution().isHappy(19))     # True
print(Solution().isHappy(10))     # True
print(Solution().isHappy(1))      # True
print(Solution().isHappy(2))      # False
print('\n')
