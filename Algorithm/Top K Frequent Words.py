"""
Given a list of words and an integer k, return the top k frequent words in the list.

Example
Example 1:

Input:
  [
    "yes", "lint", "code",
    "yes", "code", "baby",
    "you", "baby", "chrome",
    "safari", "lint", "code",
    "body", "lint", "code"
  ]
  k = 3
Output: ["code", "lint", "baby"]
Example 2:

Input:
  [
    "yes", "lint", "code",
    "yes", "code", "baby",
    "you", "baby", "chrome",
    "safari", "lint", "code",
    "body", "lint", "code"
  ]
  k = 4
Output: ["code", "lint", "baby", "yes"]
Challenge
Do it in O(nlogk) time and O(n) extra space.

Notice
You should order the words by the frequency of them in the return list, the most frequent one comes first.
If two words has the same frequency, the one with lower alphabetical order come first.
"""


class Solution:
    """
    @param words: an array of string
    @param k: An integer
    @return: an array of string
    """

    """
    思路过程：
    要求先按cnt排序再按alphabetical 排序


    O(N) 时间扫一遍list并存在一个dict{word: cnt}
    直接能想到的就是扫一遍sort value in dict, 然后把word一个个
    展开并存到heapq里按照value大小以及alphabetical大小，
    最后返回nsmallest
    Time: O(NLOGN), Space:O(M) 
    """

    def topKFrequentWords(self, words, k):
        # write your code here
        ## corner cases
        if words is None or len(words) == 0:
            return []

        if len(words) == 1:
            return words

        ## scan list and get word count dict
        word_dict = {}
        for word in words:
            if word not in word_dict:
                word_dict[word] = 1
            else:
                word_dict[word] += 1

                ## scan dict values and save into heapq
        from heapq import nsmallest, heappush, heappop
        heap = []
        for word in word_dict:
            heappush(heap, (-word_dict[word], word))

        # returnlist = []
        # for freq, word in nsmallest(k, heap):
        #     returnlist.append(word)

        # return returnlist

        """
        or we can write as :

        """
        return [word for freq, word in nsmallest(k, heap)]