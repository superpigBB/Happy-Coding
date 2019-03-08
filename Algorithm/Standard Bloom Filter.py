"""
Implement a standard bloom filter. Support the following method:

StandardBloomFilter(k),The constructor and you need to create k hash functions.
add(string). add a string into bloom filter.
contains(string). Check a string whether exists in bloom filter.
Example
Example1

Input:
CountingBloomFilter(3)
add("lint")
add("code")
contains("lint")
remove("lint")
contains("lint")

Output:
[true,false]
Example2

Input:
CountingBloomFilter(3)
add("lint")
add("lint")
contains("lint")
remove("lint")
contains("lint")

Output:
[true,false]
"""

import random


class HashFunction:

    def __init__(self, cap, seed):
        self.cap = cap
        self.seed = seed

    def hash(self, value):
        ret = 0
        for i in value:
            ret += self.seed * ret + ord(i)
            ret %= self.cap

        return ret


class StandardBloomFilter:

    # @param {int} k an integer
    def __init__(self, k):
        # initialize your data structure here
        self.bitset = dict()
        self.hashFunc = []
        for i in range(k):
            self.hashFunc.append(HashFunction(random.randint(10000, 20000), i * 2 + 3))

    # @param {str} word a string
    def add(self, word):
        # Write your code here
        for f in self.hashFunc:
            position = f.hash(word)
            self.bitset[position] = 1


    # @param {str} word a string
    # @return {bool} True if word is exists in bllom filter or false
    def contains(self, word):
        # Write your code here
        for f in self.hashFunc:
            position = f.hash(word)
            if position not in self.bitset:
                return False

        return True