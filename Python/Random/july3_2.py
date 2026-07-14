'''
Q2 — Easy-Medium
You are given a list of strings. Group the words that are anagrams of each other together. 
Return a list of groups.
Input:  ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
'''
from collections import defaultdict
given=input().split()
mydict=defaultdict(list)

for word in given: #o(n)
    key="".join(sorted(word)) #o(m log m)
    if key in mydict:
        mydict[key].append(word)
    else:
        mydict[key].append(word)
result=[value for value in mydict.values()]
print(result)

#tc=o(n)*o(m log m) = o(m log m) sc=o(n)


 