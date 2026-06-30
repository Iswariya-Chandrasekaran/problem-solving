'''
Q3 — Medium

Given a string, find the first non-repeating character and return it. If none, return "_".
Input: "aabbcde"
Output: "c"
'''
from collections import Counter
word=input()
d=Counter(word)
def non_repeat(d):
    for key in d:
        if d[key]==1:
            return key
    return "_"
print(non_repeat(d))

# tc = o(n) sc = O(n)