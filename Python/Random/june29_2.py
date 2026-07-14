'''
Q2 — Easy-Medium
Given a sentence, return the word with the maximum length. If tie, return the first one.
Input: "I love backend development "
Output: "development"
'''
sentence=input().split()
# tc = o(n log n) sc = o(n)
by_length=sorted(sentence, key=len, reverse=True)
# tc= o(n) sc = (1)
bylength=max(sentence,key=len)
print(by_length[0],bylength)

