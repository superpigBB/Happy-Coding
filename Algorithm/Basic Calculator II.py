# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.
#
# You may assume that the given expression is always valid.
#
# Some examples:
# "3+2*2" = 7
# " 3/2 " = 1
# " 3+5 / 2 " = 5
# Note: Do not use the eval built-in library function.

### Solution1: split string into nums list and symbols list then process numbers connected with * or /,
### Time O(N) Space O(N)

class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        ## remove all spaces in string
        i = 0
        num_str = ""
        num_list = []
        symbol_list = []
        s = s.replace(" ", "")
        while i < len(s):
            if s[i].isdigit():
                num_str = num_str + s[i]
                i += 1
                continue
            num = int(num_str)
            num_list.append(num)
            symbol_list.append(s[i])
            num_str = ''
            # print("non_digit is %s , number is %d" % (s[i], num))
            i += 1
        num = int(num_str)
        num_list.append(num)

        i = 0
        while i < len(symbol_list):
            if symbol_list[i] == "*":
                num_list[i] = num_list[i] * num_list[i + 1]
                num_list.pop(i + 1)
                symbol_list.pop(i)
            elif symbol_list[i] == '/':
                num_list[i] = num_list[i] // num_list[i + 1]
                num_list.pop(i + 1)
                symbol_list.pop(i)
            else:
                i += 1

        ## Scan symbol_list and num_list1 to get final calculation

        i = 1
        sum =  num_list[0]
        while i < len(num_list):
            if symbol_list[i - 1] == '+':
                sum += num_list[i]
            else:
                sum -= num_list[i]
            i += 1
        # print("total = %d" % sum)
        return sum


# print(Solution().calculate("30+2*2 - 3/2 + 5"))     #38
# print(Solution().calculate("3+2*2"))     #7
# print(Solution().calculate("3/2"))       #1
# print(Solution().calculate("3 + 5 / 2")) #5
# print("\n")

### Solution2: transform such string into a list with +/-, like [30 + 2 *2 - 3/2 + 5], 30 => +30, 2 * 2 =>4 , -3/2 => -1, +5 => 5
### One loop is enough
### very fast and clean
### Time O(N) Space O(N)

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        num = 0
        prev_op = '+'
        s = s + '+'
        for n in s:
            if n.isdigit():
                num = num * 10 + ord(n) - ord('0')
            elif n == ' ':
                continue
            else:
                # "3+2*2"
                if prev_op == '+':
                    stack.append(num)
                elif prev_op == '-':
                    stack.append(-num)
                elif prev_op == '*':
                    stack[-1] = stack[-1] * num
                else:
                    # in python -3 / 2 == -2, since when dividing Python uses Floor division.
                    stack[-1] = int(stack[-1] * 1.0 / num)
                num = 0
                prev_op = n
        return sum(stack)

print(Solution().calculate("30+2*2 - 3/2 + 5"))     #38
print(Solution().calculate("3+2*2"))     #7
print(Solution().calculate("3/2"))       #1
print(Solution().calculate("3 + 5 / 2")) #5
print("\n")
