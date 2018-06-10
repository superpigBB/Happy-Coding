# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.
#
# Note:
# Have you consider that the string might be empty? This is a good question to ask during an interview.
#
# For the purpose of this problem, we define empty string as valid palindrome.

### Solution1: convert string to lower or upper cases and judge if its alphanumeric by using string.isalnum()
### O(N) time O(1) space 73%
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        newstring = ""
        ## build a new string called newstring, save all alpha numeric values into that new string
        for element in s.lower():
           if element.isalnum():
               newstring += element

        return newstring == newstring[::-1]


obj = Solution()
print(obj.isPalindrome('.,'))
print(obj.isPalindrome('a.'))
print(obj.isPalindrome(' '))
print(obj.isPalindrome(''))
print(obj.isPalindrome('A man, a plan, a canal: Panama'))
print(obj.isPalindrome('race a car'))
print("\n")

### Solution 2: try to use two pointers to check from both start and end
### first submission, ignore non alnum stuff, which leads to //IndexError: string index out of range//
### second submission: wrong answer: "a."
### third submission: wrong answer: ".,"
### O(N) TIME, O(1) space

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        s = s.lower()

        i = 0
        j = len(s) - 1

        while i <= j:
            while i < len(s) - 1 and i <= j:
                if not s[i].isalnum():
                    i+=1
                else:
                    break
            while j > 0 and i <= j:
                if not s[j].isalnum():
                    j -=1
                else:
                    break
            # print ("i, j is %s %s" %(i, j), "character is %s %s" %(s[i], s[j]))
            if s[i] != s[j] and s[i].isalnum() and s[j].isalnum(): ## or it can be written as: if s[i] != s[j] and i <= j: return False
                return False
            i += 1
            j -= 1
        return True



obj = Solution()
print(obj.isPalindrome('.,'))
print(obj.isPalindrome('a.'))
print(obj.isPalindrome(''))
print(obj.isPalindrome(' ')) #IndexError: string index out of range
print(obj.isPalindrome('A man, a plan, a canal: Panama'))
print(obj.isPalindrome('race a car'))
print("\n")

### Solution3: 用Regex方法remove non-numeric/alpha chars
###但不知道给不给Import something
### O(N) TIME, O(1) SPACE
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        s = re.sub(r'[^A-Za-z0-9]', '', s).lower()
        return s == s[::-1]
