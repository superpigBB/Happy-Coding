# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
#
# Example:
# Given a = 1 and b = 2, return 3.
#
# Credits:
# Special thanks to @fujiaozhu for adding this problem and creating all test cases.

### Original Method:
### This should be basic knowledge of how to transform from decimalism to binary
### test more like computer knowledge
### decimalism can be binary=> two methods
### 1. binary = lambda n: '' if n==0 else binary(n/2) + str(n % 2)
### 2. binary = '{0:b}', format(i)
### 2 is faster
### I will directly check anwsers since no meaning for finding the rules
### int('binary', 2) => binary to decimal
### Directly copy from other solution

class Solution(object):
    def getSum(self, a, b):
        mask = 0xFFFFFFFF
        _min = 0x80000000
        while b:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        return a if a <= _min else ~(a ^ mask)

obj = Solution()
print obj.getSum(1,2)