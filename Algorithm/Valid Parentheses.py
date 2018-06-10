# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.


### Solution 1
### Time Complexity O(n/2) Space O(1)
### Exception "[({(())}[()])]"
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 1:
            return False

        i = 0
        j = len(s) - 1

        while i  < len(s) and i <= j:
            if all(s[i] != char for char in '()[]{}'):
                return False
            elif i + 1 < len(s) and ord(s[i + 1]) > ord(s[i]) and ord(s[i + 1]) - ord(s[i]) <= 2:
                i += 2
            elif ord(s[j]) > ord(s[i]) and ord(s[j]) - ord(s[i]) <= 2:
                # print("previous ", s[i], s[j])
                i += 1
                j -= 1
                # print("current", s[i], s[j])
                # print ("%d, %d" % (i, j))
            else:
                return False

        return True



# print(Solution().isValid("[({(())}[()])]"))  # True
# print(Solution().isValid('()[]{}'))  # True
# print(Solution().isValid('([{}])'))  # True
# print(Solution().isValid('()[{}]'))  # True
# print(Solution().isValid(''))        # False
# print(Solution().isValid('()[]{'))   # False
# print(Solution().isValid('()[a]'))   # False
# print('\n')

### Solution 1.2
### Time Complexity O(n) Space O(n)

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 1:
            return False

        stack = []
        for char in s:
            # if all(char != c for c in '()[]{}'):
            #     return False
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            elif not stack:
                return False
            elif ord(char) - ord(stack[-1]) <= 2 and ord(char) > ord(stack[-1]):
                stack.pop()
            else:
                return False
        if stack:
            return False
        return True



print(Solution().isValid("(])")) # False
print(Solution().isValid("[({(())}[()])]"))  # True
print(Solution().isValid('()[]{}'))  # True
print(Solution().isValid('([{}])'))  # True
print(Solution().isValid('()[{}]'))  # True
print(Solution().isValid(''))        # False
print(Solution().isValid('()[]{'))   # False
print(Solution().isValid('()[a]'))   # False
print('\n')

### Solution 2
### Time Complexity O(n) Space O(n)
### Copy from Jiuzhang but one thing it doesn't consider is: null

class Solution(object):
    '''
    题意：输入一个只包含括号的字符串，判断括号是否匹配
    模拟堆栈，读到左括号压栈，读到右括号判断栈顶括号是否匹配
    '''
    def isValid(self, s):
        stack = []
        for ch in s:
            # 压栈
            if ch == '{' or ch == '[' or ch == '(':
                stack.append(ch)
            else:
                # 栈需非空
                if not stack:
                    return False
                # 判断栈顶是否匹配
                if ch == ']' and stack[-1] != '[' or ch == ')' and stack[-1] != '(' or ch == '}' and stack[-1] != '{':
                    return False
                # 弹栈
                stack.pop()
        return not stack


print(Solution().isValid("(])")) # False
print(Solution().isValid("[({(())}[()])]"))  # True
print(Solution().isValid('()[]{}'))  # True
print(Solution().isValid('([{}])'))  # True
print(Solution().isValid('()[{}]'))  # True
print(Solution().isValid(''))        # False
print(Solution().isValid('()[]{'))   # False
print(Solution().isValid('()[a]'))   # False
print('\n')