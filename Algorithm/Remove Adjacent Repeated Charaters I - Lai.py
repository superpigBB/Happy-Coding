"""
Remove adjacent, repeated characters in a given string, leaving only one character for each group of such characters.

Assumptions

Try to do it in place.
Examples

“aaaabbbc” is transferred to “abc”
Corner Cases

If the given string is null, returning null or an empty string are both valid.
"""

class Solution(object):
    """
    解题思路：两根指针，一根追踪非重复，另一个动态追踪直到第一个重复结束然后直到结尾; 因为string是immutable=> we can transform to list
    first; 然后用in place来改变一个list并最后转为string
    Time: O(n)
    Space: O(n)
    """
    def deDup(self, input):
        """
        input: string input
        return: string
        """
        # write your solution here
        """Corner Cases"""
        if input is None or len(input) <= 1:
            return input

        start = 0  # start index for a in-place list
        # move = 0
        # input_list = list(input)
        # while move < len(input_list):
        #     if input_list[move] != input_list[start]:
        #         start += 1
        #         input_list[start] = input_list[move]
        #
        #     move += 1

        # input_list = input_list[: start + 1]
        # return ''.join(input_list)

        """ from 33 to 43 can also be re-written as the following"""
        input_list = list(input)
        for move in range(len(input_list)):
            if input_list[move] != input_list[start]:
                start += 1
                input_list[start] = input_list[move]

        input_list = input_list[: start + 1]
        return ''.join(input_list)

print(Solution().deDup('aaaabbbc'))   # 'abc'
print(Solution().deDup(''))   # ''
print(Solution().deDup('a'))   # 'a'

