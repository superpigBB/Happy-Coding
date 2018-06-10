# Write a function to find the longest common prefix string amongst an array of strings.


### Solution 1: found error, corrected in Solution 1.2
### Time O(CN) Space O（N）
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        looplen = len(min(strs))  #  wrong! Line 12: ValueError: min() arg is an empty sequence
        totalstring = ''

        for i in range(looplen):
            samecnt = 1
            character  = strs[0][0]

            for string in strs[1:]:
                if string[0] != character:
                    return totalstring
                else:
                    samecnt += 1
            if samecnt == len(strs):
                totalstring += character

            strs = [str[1:] for str in strs]

        return totalstring

# print(Solution().longestCommonPrefix([]))                                   # ''
# print(Solution().longestCommonPrefix(["abc", "c", "dsdfwd"]))               # ''
# print(Solution().longestCommonPrefix(["abc", "abcdesfds", "abfsdfs"]))      # ab
# print(Solution().longestCommonPrefix(["abc", "ab", ""]))                    # ''
# print(Solution().longestCommonPrefix(["abcdsfsdf", "abcd", "abcdefsdf"]))   # abcd
# print("\n")


### Solution 1.2:
### Time O(CN) Space O（N）
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        looplen = len(min(strs))
        totalstring = ''

        for i in range(looplen):
            samecnt = 1
            character  = strs[0][0]

            for string in strs[1:]:
                if string[0] != character:
                    return totalstring
                else:
                    samecnt += 1
            if samecnt == len(strs):
                totalstring += character

            strs = [str[1:] for str in strs]

        return totalstring

# print(Solution().longestCommonPrefix([]))                                   # ''
# print(Solution().longestCommonPrefix(["abc", "c", "dsdfwd"]))               # ''
# print(Solution().longestCommonPrefix(["abc", "abcdesfds", "abfsdfs"]))      # ab
# print(Solution().longestCommonPrefix(["abc", "ab", ""]))                    # ''
# print(Solution().longestCommonPrefix(["abcdsfsdf", "abcd", "abcdefsdf"]))   # abcd
# print("\n")


### Solution 1.3:
### Time O(CN) Space O（1）
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        looplen = len(min(strs))
        # totalstring = ''
        end = 0

        for i in range(looplen):
            samecnt = 1
            character  = strs[0][i]

            for string in strs[1:]:
                if string[i] != character:
                    return strs[0][:end]
                else:               # 可写可不写
                    samecnt += 1    # 可写可不写
            if samecnt == len(strs):# 可写可不写
                end += 1
                # print(end)

            # strs = [str[1:] for str in strs]

        return strs[0][:end]

# print(Solution().longestCommonPrefix([]))                                   # ''
# print(Solution().longestCommonPrefix(["abc", "c", "dsdfwd"]))               # ''
# print(Solution().longestCommonPrefix(["abc", "abcdesfds", "abfsdfs"]))      # ab
# print(Solution().longestCommonPrefix(["abc", "ab", ""]))                    # ''
# print(Solution().longestCommonPrefix(["abcdsfsdf", "abcd", "abcdefsdf"]))   # abcd
# print("\n")


### Solution 2: sort strs to compare the first one and last one since sort alphabetically
### Time O(N), Space O(N)
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''

        common_prefix = ''
        strs = sorted(strs)
        ## comp first and last string only and find common prefix
        first_str = strs[0]
        last_str = strs[-1]

        for i in range(len(first_str)):
            if first_str[i] == last_str[i]:
                common_prefix += first_str[i]
            else:
                return common_prefix
        return common_prefix


#
# print(Solution().longestCommonPrefix([]))                                   # ''
# print(Solution().longestCommonPrefix(["abc", "c", "dsdfwd"]))               # ''
# print(Solution().longestCommonPrefix(["abc", "abcdesfds", "abfsdfs"]))      # ab
# print(Solution().longestCommonPrefix(["abc", "ab", ""]))                    # ''
# print(Solution().longestCommonPrefix(["abcdsfsdf", "abcd", "abcdefsdf"]))   # abcd
# print("\n")

### Solution 2.1: sort strs to compare the first one and last one since sort alphabetically
### Time O(N), Space O(1)
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''

        # common_prefix = ''
        end = 0
        strs = sorted(strs)
        ## comp first and last string only and find common prefix
        first_str = strs[0]
        last_str = strs[-1]

        for i in range(len(first_str)):
            if first_str[i] == last_str[i]:
                end += 1
            else:
                return strs[0][:end]
        return strs[0][:end]



print(Solution().longestCommonPrefix([]))                                   # ''
print(Solution().longestCommonPrefix(["abc", "c", "dsdfwd"]))               # ''
print(Solution().longestCommonPrefix(["abc", "abcdesfds", "abfsdfs"]))      # ab
print(Solution().longestCommonPrefix(["abc", "ab", ""]))                    # ''
print(Solution().longestCommonPrefix(["abcdsfsdf", "abcd", "abcdefsdf"]))   # abcd
print("\n")


### Solution 3: online method, use enumerate and zip
### Time O(N), Space O(1)
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        for i, chars in enumerate(zip(*strs)):
            if len(set(chars)) > 1:
                return strs[0][:i]

        return min(strs)


# print(Solution().longestCommonPrefix([]))                                   # ''
# print(Solution().longestCommonPrefix(["abc", "c", "dsdfwd"]))               # ''
# print(Solution().longestCommonPrefix(["abc", "abcdesfds", "abfsdfs"]))      # ab
# print(Solution().longestCommonPrefix(["abc", "ab", ""]))                    # ''
# print(Solution().longestCommonPrefix(["abcdsfsdf", "abcd", "abcdefsdf"]))   # abcd
# print("\n")