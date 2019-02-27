"""
Create an inverted index with given documents.

Example
Given a list of documents with id and content. (class Document)
Return an inverted index (HashMap with key is the word and value is a list of document ids).
Example 1:

Input:
[
  {
    "id": 1,
    "content": "This is the content of document 1 it is very short"
  },
  {
    "id": 2,
    "content": "This is the content of document 2 it is very long bilabial bilabial heheh hahaha ..."
  },
]
Output:
{
   "This": [1, 2],
   "is": [1, 2],
   ...
}
Example 2:

Input:
[
  {
    "id": 1,
    "content": "you are young"
  },
  {
    "id": 2,
    "content": "you are handsome"
  },
]
Output:
{
   "are": [1, 2],
   ...
}
Notice
Ensure that data does not include punctuation.
"""
'''
Definition of Document
class Document:
    def __init__(self, id, cotent):
        self.id = id
        self.content = content
'''
"""
思路过程：
input: given list->[Document class: id/content]
output: dict{word:[ids...]}
逐个scan list里的class元素，设置defaultdict的int来存每个单词的ids
id是不重复的吧？否则直接用append做会有问题? 
=》如果id有重复，就再建一个dict来存id set,看id存不存在，因为set查询的时间复杂度为O(1)
if not found, can we assume returned value == {} if not found? 
Time: O(nm), Space: O(size of dict)
"""


class Solution:
    # @param {Document[]} docs a list of documents
    # @return {dict(string, int[])} an inverted index
    def invertedIndex(self, docs):
        # Write your code here
        ## initialize dict/import re
        from collections import defaultdict
        dict = defaultdict(list)  ##这里用不用defaultdict无所谓
        ## corner cases
        if docs is None or len(docs) == 0:
            return dict

        for doc in docs:
            id = doc.id
            content = doc.content
            for word in content.split():
                if word in dict:
                    if dict[word][-1] != id:
                        dict[word].append(id)
                else:
                    dict[word] = [id]

        return dict




