'''
Given a string, return the first character that appears only once.

If no such character exists, return None.

Example 1
s = "leetcode"

Output:
'l' 
'''
from collections import Counter

s= input()
count = Counter(s)

def non_repeating(count):
    for key, value in count.items():
        if value == 1:
            return key
    return None
    
print(non_repeating(count))