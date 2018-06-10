# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
# Example:
#
# Input: "babad"
#
# Output: "bab"
#
# Note: "aba" is also a valid answer.
#
#
#
# Example:
#
# Input: "cbbd"
#
# Output: "bb"

#Solutions Summary:
# Solution 1/1.1: 中心点枚举法
# Solution 2: Manachester's algorithm O(n)
# Solution 3: Suffix Array O(nlogn)
# Solution 3: dynamic programing
# Solution 4: brute force


## Solution 1 (中心点枚举法： Recommend)
## 类似前面那个solution, 利用palindrome数长度的奇偶性来选取中心店
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ## Corner Cases
        if s is None:
            return ''
        if len(s) == 1 or len(s) == 0:
            return s

        maxLen, maxStart = 0, 0
        for i in range(len(s)):
            ## 长度为odd number
            palindromeLen = self.longestPalindromeLen(s, i, i)
            if palindromeLen > maxLen:
                maxLen = palindromeLen
                start = i - palindromeLen // 2

            ## 长度为even number
            palindromeLen = self.longestPalindromeLen(s, i, i + 1)
            if palindromeLen > maxLen:
                maxLen = palindromeLen
                start = i - palindromeLen // 2 + 1

        return s[start: start + maxLen]

    def longestPalindromeLen(self, s, left, right):
        palindromeLen = 0
        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                break
            if left == right:
                palindromeLen += 1
            else:
                palindromeLen += 2
            left -= 1
            right += 1
        return palindromeLen


## Solution1.1: loop每个字母并以每个字母为中心，向两端扩散看是否是palindrome并最长 (中心点枚举法： 没有solution 1好， 因为有重复代码)
## Time: O(N^2), Space: O(1)
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ## corner cases:
        if len(s) == 1 or len(s) == 0:
            return s

        maxStr = ''
        maxLen = 0
        for i in range(len(s) - 1):
            ## 根据 s[i + 1] 是否和s[i]相等，分奇数长度和偶数长度

            ## even len
            # print "current i:", i
            if s[i + 1] == s[i]:
                if i - 1 < 0 or i + 2 >= len(s):
                    if 2 > maxLen:
                        maxStr = s[i: i + 2]
                        maxLen = 2
                        # print("1: ", maxStr)
                else:
                    left, right = i - 1, i + 2
                    while left >= 0 and right < len(s):
                        if s[left] != s[right]:
                            break
                        left -= 1
                        right += 1

                    left, right = left + 1, right - 1
                    if right - left + 1 > maxLen:
                        maxLen = right - left + 1
                        maxStr = s[left: right + 1]
                        # print('2: ', maxStr)
            # print ("max string len is ", maxLen)
            # print ("i is ", i)
            ## odd len
            if i - 1 < 0 or i + 1 >= len(s):
                if 1 > maxLen:
                    maxStr = s[i]
                    maxLen = 1
                    # print('3: ', maxStr)

            else:
                # print ('3: i is ', i)
                left, right = i - 1, i + 1
                # print ("3 : left is %d right is %d " %(left, right))
                while left >= 0 and right < len(s):
                    if s[left] != s[right]:
                        break
                    left -= 1
                    right += 1

                left, right = left + 1, right - 1
                # print("left is %d right is %d" % (left, right))
                if right - left + 1 > maxLen:
                    maxLen = right - left + 1
                    maxStr = s[left: right + 1]
                    # print('4: ', maxStr)

        return maxStr
        # print (maxStr)


# print (Solution().longestPalindrome('abcdzdca'))





### Solution 2: Manacher's algorithm：可以背！网上的答案！ O(N)时间求字符串的最长回文子串 https://www.felix021.com/blog/read.php?2040
###

## example
# "babad"
# "ccc"
# "abcdzdcab"
# "abcda"

## expected
# "bab"
# "ccc"
# "cdzdc"
# "a"

## Solution 3: suffix array

## Solution 4: dynamic programming

## solution 5: 从头开始遍历i = 0, j = i + 1 但小于len(s) =》 类似双指针 => 比较推荐solution 1/1.1
## Lintcode 过了， leetcode 没过！
## Time O(N^3), Space O(1)
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ## corner cases
        if len(s) == 1 or len(s) == 0:
            return s
        if self.isPalindrome(s, 0, len(s) - 1):
            return s

        maxLen = 0
        maxstr = ''
        for i in range(len(s) - 1):
            j = i
            while j < len(s):
                if self.isPalindrome(string=s, start=i, end=j) and j - i + 1 > maxLen:
                    maxstr = s[i: j + 1]
                    maxLen = j - i + 1
                j += 1
        return maxstr

    ## 相向双指针: 判断是否是palindrome=>time: O(end - start)
    def isPalindrome(self, string, start, end):
        while start <= end:
            if string[start] != string[end]:
                return False
            start += 1
            end -= 1
        return True

