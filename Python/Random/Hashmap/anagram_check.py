'''
july 2 - Medium
3. You are given two strings. Check if they are anagrams of each other. Two strings 
are anagrams if they contain the same characters with the same frequency 
(ignore spaces, case insensitive).
Input:  "listen", "silent"
Output: True
Input:  "hello", "world"
Output: False
'''
str1=input().strip().lower()
str2=input().strip().lower()
freq={}
def anagram(str1,str2):
    for ch in str1:
        freq[ch]=freq.get(ch,0)+1

    for ch in str2:
        freq[ch]=freq.get(ch,0)-1

    print(freq)
    for value in freq.values():
        if value!=0:
            return False
    return True   
        
print(anagram(str1,str2))

#tc = o(n) sc=o(n)