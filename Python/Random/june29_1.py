'''
Q1 — Easy
Given a string, check if it is a palindrome. Return True or False.
Input: "racecar"
Output: True

Input: "hello"
Output: False
'''
word=input()
if word[::-1]==word:
    print("True")
else:
    print("False")
# tc = o(n) sc = o(n)

def fnpalidrome(word):
    left=0
    right=len(word)-1
    while left<right:
        if word[left]!=word[right]:
            return False
        left+=1
        right-=1
    return True

print(fnpalidrome(word))

# tc = o(n) sc = o(1)