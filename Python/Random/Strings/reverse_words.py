'''
june 28 — Easy-Medium
2. Given a string, reverse only the words, not the characters.
Input: "hello world"
Output: "world hello"
'''
sentence=input().split()
rev=reversed(sentence)
print(" ".join(rev))

# tc = o(n) sc = o(n)