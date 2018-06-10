### Leetcode
# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence
# from beginWord to endWord, such that:
#
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# Note:
#
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# Example 1:
#
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# Output: 5
#
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
# Example 2:
#
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# Output: 0
#
# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

### Solution1 (recommended)
##求最短路径并且每次变化都是1=》BFS
##传统双向分层遍历（格式推荐：容易解释）
## time O(26 * len(word) * len(word))
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        ## exceptions exclusion

        ## set wordList as set first => which i think the key to make script not exceeding time limit
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        ## initialize start_queue and end_queue for BFS
        from collections import deque
        start_queue = deque([beginWord])
        end_queue = deque([endWord])

        ## initialize start_set and end_set
        start_set = {beginWord}
        end_set = {endWord}

        ## initialize level count
        level_cnt = 1

        while start_queue or end_queue:
            start_size = len(start_queue)
            end_size = len(end_queue)

            for i in range(start_size):
                word = start_queue.popleft()
                if word in end_set:
                    return level_cnt
                for neighbor in self.word_neighbors(word, wordSet):
                    if neighbor in start_set:
                        continue
                    start_set.add(neighbor)
                    start_queue.append(neighbor)

            level_cnt += 1

            for i in range(end_size):
                word = end_queue.popleft()
                if word in start_set:
                    return level_cnt
                for neighbor in self.word_neighbors(word, wordSet):
                    if neighbor in end_set:
                        continue
                    end_set.add(neighbor)
                    end_queue.append(neighbor)

            level_cnt += 1

        return 0

    ## find all possible words when change 1 letter for each index of the word
    def word_neighbors(self, word, wordSet):
        ## set neighbors set
        neighbors = set()
        for index in range(len(word)):
            letter = word[index]
            for c in set('abcdefghijklmnopqrstuvwxyz'):
                if c == letter:
                    continue
                ## replace chr(num) with letter
                word_updated = word[:index] + c + word[index + 1:]
                if word_updated in wordSet:
                    neighbors.add(word_updated)
        return neighbors

## Solution 2
##求最短路径并且每次变化都是1=》BFS
##传统分层遍历 （格式推荐: 比较好解释）
## time O(26 * len(word) * len(word))
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        ## exceptions exclusion
        wordset = set(wordList)
        if endWord not in wordList:
            return 0
        ## initialize words queue for BFS
        from collections import deque
        words_queue = deque([beginWord])

        level_cnt = 0
        while words_queue:
            level_size = len(words_queue)
            level_cnt += 1
            for i in range(level_size):
                word = words_queue.popleft()
                # print(word)
                # print(level_cnt)
                if word == endWord:
                    return level_cnt
                for neighbor in self.word_neighbors(word, wordset):
                    words_queue.append(neighbor)

        return 0

    ## find all possible words when change 1 letter for each index of the word
    def word_neighbors(self, word, wordset):
        ## set neighbors set
        neighbors = set()
        for index in range(len(word)):
            letter = word[index]
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c == letter:
                    continue
                ## replace chr(num) with letter
                word_updated = word[:index] + c + word[index + 1:]
                if word_updated in wordset:
                    neighbors.add(word_updated)
                    wordset.remove(word_updated)
        return neighbors

## Solution 3
## 另一种形式的双向遍历: 比传统双向遍历还要快很多
## 永远遍历最短的set, beginset永远是最短的那个level
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordset = set(wordList)
        ## exceptions
        if endWord not in wordset:
            return 0

        ## initialize sets: beginSet/endSet
        beginSet = {beginWord}
        endSet = {endWord}

        level_cnt = 1

        while beginSet:
            ## beginSet should be shortest set
            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet
            ## initialize levelSet
            levelSet = set()

            ## loop every word in beginSet
            for word in beginSet:
                ## replace a-z for each part of the word
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c == word[i]:
                            continue
                        newWord = word[:i] + c + word[i + 1:]

                        if newWord in endSet:
                            return level_cnt + 1

                        if newWord in wordset:
                            wordset.remove(newWord)
                            levelSet.add(newWord)

            beginSet = levelSet
            level_cnt += 1

        return 0

## Solution 4
##求最短路径并且每次变化都是1=》BFS
##分层遍历 => 如果分层遍历减少一次循环
## time O(26 * len(word) * len(word))
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        ## exceptions exclusion
        wordset = set(wordList)
        if endWord not in wordList:
            return 0
        ## initialize words queue for BFS
        from collections import deque
        ## a tuple saved in queue, 1 represent level_cnt = 1
        words_queue = deque([(beginWord, 1)])

        while words_queue:
            word, level_cnt = words_queue.popleft()
            # print("word: %s Level: %d" %(word, level_cnt))
            if word == endWord:
                return level_cnt
            ## 对每个单词进行每个位置character与其余25个字母互换一次
            for i in range(len(word)):
                letter = word[i]
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c != letter:
                        word_updated = word[:i] + c + word[i + 1:]
                        if word_updated in wordset:
                            words_queue.append((word_updated, level_cnt + 1))
                            wordset.remove(word_updated)

        return 0






########################################################################################################################3
### Lintcode
# Description
# Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that:
#
# Only one letter can be changed at a time
# Each intermediate word must exist in the dictionary
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# Have you met this question in a real interview?
# Example
# Given:
# start = "hit"
# end = "cog"
# dict = ["hot","dot","dog","lot","log"]
# As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.



class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """

    def ladderLength(self, start, end, dict):
        # write your code here
        ## exceptions exclusion
        if start == end:
            return 1

        ## add end word into set dict
        dict.add(end)

        ## initialize visited words and words queue for BFS
        visited_words = {start: 1}
        words_queue = [start]

        level_cnt = 1
        while words_queue:
            level_size = len(words_queue)
            level_cnt += 1
            for i in range(level_size):
                word = words_queue.pop(0)
                for neighbor in self.word_neighbors(word, dict):
                    if neighbor not in visited_words:
                        if neighbor == end:
                            return level_cnt
                        words_queue.append(neighbor)
                        visited_words[neighbor] = 1

        return 0

    ## find all possible words when change 1 letter for each index of the word
    def word_neighbors(self, word, dict):
        neighbors = []
        for index in range(len(word)):
            letter = word[index]
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c == letter:
                    continue
                ## replace chr(num) with letter
                word_updated = word[:index] + c + word[index + 1:]
                if word_updated in dict:
                    neighbors.append(word_updated)
        return neighbors
