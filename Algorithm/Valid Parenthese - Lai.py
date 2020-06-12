"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
The brackets must close in the correct order.

Examples

"()" and "()[]{}", "[{()}()]" are all valid but "(]" and "([)]" are not.
"""


class Solution(object):
    """
    解题思路: 建一个stack来存遇到的一半符号，一旦遇到符号的另一半，则Pop出stack里的那个，知道遍历完
    如果stack里最后not empty, 则False =》 stack是用来往回遍历的
    Time: O(N)
    Space: O(N)
    """
    def isValid(self, input):
        """
        input: string input
        return: boolean
        """
        # write your solution here
        """Corner Cases"""
        if not input:   # input == '' or input is None
            return True
        if len(input) == 1:
            return False

        stack = list()
        # dict to save pair characters
        char_dict = {'(': ')', '{': '}', '[':']'}

        for e in input:
            if e in char_dict:    #只要是char_dict里值，就加进stack
                stack.append(e)
            else:                 # ), }, ]
                if len(stack) == 0:
                    return False
                else:
                    last_stack = stack[-1]
                    if char_dict[last_stack] == e:   # if match
                        stack.pop()
                    else:    # not match
                        return False


        if len(stack) == 0:
            return True
        else:
            return False



print(Solution().isValid('}}}{{{'))  # False
print(Solution().isValid('()'))  # True
print(Solution().isValid('()[]{}'))  # True
print(Solution().isValid('([)]'))  # False
print(Solution().isValid('(]'))  # False
