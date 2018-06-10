# Implement strStr().
#
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
# Example 1:
#
# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:
#
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1


### Solution1: use find in string; 记得要想到exception: target or source is None/Null
### Time O(N), Space O(1)
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack is None or needle is None:
            return -1
        return haystack.find(needle)

# print(Solution().strStr('hello', 'll'))   #2
# print(Solution().strStr('aaaaa', 'bba'))  #-1
# print(Solution().strStr('aaaaa', None))   #-1
# print(Solution().strStr(None, 'bba'))     #-1
# print('\n')


### Solution2: use two pointers
## Time O(NM), Space O(1)

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack is None or needle is None:
            return -1

        ## set one pointer i at haystack, another j at needle
        for i in range(len(haystack) - len(needle) +1):
            j = 0
            while j < len(needle):
                if haystack[i + j] != needle[j]:
                    j = 0
                    break
                else:
                    j += 1
            if j == len(needle):
                return i

        return -1


print(Solution().strStr("mississippi", "issipi")) #-1
print(Solution().strStr("mississippi","issip")) #4
print(Solution().strStr('hello', 'll'))   #2
print(Solution().strStr('aaaaa', 'bba'))  #-1
print(Solution().strStr('aaaaa', None))   #-1
print(Solution().strStr(None, 'bba'))     #-1
print('\n')


### Solution3: take advantage of string property in python: from online version
### Time O(NM) Space O(1)
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack is None or needle is None:
            return -1

        lh, ln = len(haystack), len(needle)
        for i in range(lh - ln + 1):
            if haystack[i:i + ln] == needle[:]:
                return i
        return -1

# print(Solution().strStr("mississippi", "issipi")) #-1
# print(Solution().strStr("mississippi","issip")) #4
# print(Solution().strStr('hello', 'll'))   #2
# print(Solution().strStr('aaaaa', 'bba'))  #-1
# print(Solution().strStr('aaaaa', None))   #-1
# print(Solution().strStr(None, 'bba'))     #-1
# print('\n')
