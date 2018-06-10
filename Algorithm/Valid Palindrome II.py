# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
#
# Example 1:
# Input: "aba"
# Output: True
# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
# Note:
# The string will only contain lowercase characters a-z. The maximum length of the string is 50000.


# ### Solution 1: use two pointers and counting deletable char, when the counting > 1, then it should be false
# ### Time O(N), Space O(1) I think it should be fast
# ### It's wrong, so updates is in Solution 2
# class Solution:
#     def validPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         if len(s) <= 2:
#             return True
#         ## define deletable char count
#         delete_cnt = 0
#         i, j = 0, len(s) - 1
#
#         while i < j :
#             if s[i] != s[j]:
#                 delete_cnt += 1
#                 if delete_cnt > 1:
#                     # print ("i, j is %d %d" %(i, j))
#                     return False
#
#                 if s[i + 1] == s[j]:
#                     i += 1
#                 elif s[i] == s[j- 1]:
#                     j -= 1
#                 else:
#                     # print ("test2: i, j is %d %d" %(i, j))
#                     return False
#
#             i += 1
#             j -= 1
#         return True
#
# # print (Solution().validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga")) ## Wrong answer when use this sample
# # s = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga" ## since cu uc, can be both i += 1 and j -=1
# # print (s[21], s[80])
# # print (Solution().validPalindrome('eccer')) ## Wrong answer when use this sample
# # print (Solution().validPalindrome('abc'))
# # print (Solution().validPalindrome('ab'))
# # print (Solution().validPalindrome('abcca'))
# # print (Solution().validPalindrome('abca'))
# # print (Solution().validPalindrome('abcde'))
# # print ("\n")

### Solution 2: updates from Solution 1 since Solution 1 miss many aspects
### Time O(N), Space O(1) I think it should be fast
class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 2:
            return True
        ## define deletable char count
        delete_cnt = 0
        i, j = 0, len(s) - 1

        while i < j:
            if s[i] != s[j]:
                if s[i:j][::-1] == s[i:j] or s[i+1: j + 1][::-1] == s[i + 1: j + 1]:
                    return True
                else:
                    return False

            i += 1
            j -= 1
        return True


print (Solution().validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga")) ## Wrong answer when use this sample
# s = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga" ## since cu uc, can be both i += 1 and j -=1
# print (s[21], s[80])
print (Solution().validPalindrome('eccer')) ## Wrong answer when use this sample
print (Solution().validPalindrome('abc'))
print (Solution().validPalindrome('ab'))
print (Solution().validPalindrome('abcca'))
print (Solution().validPalindrome('abca'))
print (Solution().validPalindrome('abcde'))
print ("\n")

### Solution 3: separate into two different functions劝分不劝合法，使得代码看上去简洁
### Time O(N), Space O(1) should be faster than Solution2, but not working on my side Lol!
### After read http://blog.csdn.net/liuxiao214/article/details/78034459, it gives a clear clue to write down the recursive call!
### and http://www.cnblogs.com/grandyang/p/7618468.html as another reference
### Set up another function called ispalindrome(s)

class Solution:
    def ispalindrome(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False

            i += 1
            j -= 1
        return True

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 2:
            return True
        ## define deletable char count
        delete_cnt = 0
        i, j = 0, len(s) - 1
        delete_cnt = 0

        while i < j:
            if s[i] != s[j]:
                delete_cnt = 1
                s1 = s[i:j]
                s2 = s[i+1: j+1]

                return Solution().ispalindrome(s1) or Solution().ispalindrome(s2)
            i += 1
            j -= 1
        return True


print (Solution().validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga")) ## Wrong answer when use this sample ## True
# s = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga" ## since cu uc, can be both i += 1 and j -=1
# print (s[21], s[80])
print (Solution().validPalindrome('eccer')) ## Wrong answer when use this sample ## True
print (Solution().validPalindrome('abc')) ## False
print (Solution().validPalindrome('ab'))  ## False
print (Solution().validPalindrome('abcca')) ## True
print (Solution().validPalindrome('abca'))  ## True
print (Solution().validPalindrome('abcde'))  ## False
print ("\n")


### Solution4: I think it's the same Solution2, but the speed is faster, I think it's  it might be caused by the range
### one is len(s) / 2, another one: best is len(s)/2
class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == s[-1::-1]: return True
        for i in range(int(len(s) / 2)):
            if s[i] != s[-1 - i]:

                new_s1 = s[:i] + s[i + 1:]
                if new_s1 == new_s1[-1::-1]: return True
                new_s2 = s[:-1 - i] + s[len(s) - i:]

                if new_s2 == new_s2[-1::-1]:
                    return True
                else:
                    return False

print (Solution().validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga")) ## Wrong answer when use this sample
# s = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga" ## since cu uc, can be both i += 1 and j -=1
# print (s[21], s[80])
print (Solution().validPalindrome('eccer')) ## Wrong answer when use this sample
print (Solution().validPalindrome('abc'))
print (Solution().validPalindrome('ab'))
print (Solution().validPalindrome('abcca'))
print (Solution().validPalindrome('abca'))
print (Solution().validPalindrome('abcde'))
print ("\n")
