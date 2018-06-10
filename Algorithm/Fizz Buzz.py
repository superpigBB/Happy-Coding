# coding=utf-8
# Write a program that outputs the string representation of numbers from 1 to n.
#
# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”.
# For numbers which are multiples of both three and five output “FizzBuzz”.
#
# Example:
#
# n = 15,
#
# Return:
# [
#     "1",
#     "2",
#     "Fizz",
#     "4",
#     "Buzz",
#     "Fizz",
#     "7",
#     "8",
#     "Fizz",
#     "Buzz",
#     "11",
#     "Fizz",
#     "13",
#     "14",
#     "FizzBuzz"
# ]

### Original Method
### I think it's an another math problem, like reverse integer
### should conisder 3 * 5 first
### 72ms 62%

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        l = []
        for num in xrange(1, n + 1):
            if num % 15 == 0:
                num = 'FizzBuzz'
            elif num % 5 == 0:
                num = 'Buzz'
            elif num % 3 == 0:
                num = 'Fizz'
            l.append(str(num))
        return l


### Method 2: the same complexity but directly append each string when execute if else
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        output = []
        for i in range(1, n+1):
            if i % 15 == 0:
                output.append("FizzBuzz")
            elif i % 5 == 0:
                output.append("Buzz")
            elif i % 3 == 0:
                output.append("Fizz")
            else:
                output.append(str(i))
        return output

obj = Solution()
print obj.fizzBuzz(15)

