'''
Q1 — Easy
You are given a string. Return a dictionary containing the frequency of each character in the string. Ignore spaces.
Input:  "hello world"
Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
'''
given= input()
freq={}

for ch in given:
    if ch !=" ":
        freq[ch]=freq.get(ch,0)+1
print(freq)

#tc= o(n) sc=o(n)