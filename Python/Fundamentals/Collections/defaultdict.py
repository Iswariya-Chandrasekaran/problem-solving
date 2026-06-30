"""
In this challenge, you will be given 2 integers, n and m. There are n words, 
which might repeat, in word group A. There are m words belonging to word group B. 
For each m words, check whether the word has appeared in group A or not. 
Print the indices of each occurrence of m in group A . If it does not appear, print -1.
Sample Input
STDIN   Function
-----   --------
5 2     group A size n = 5, group B size m = 2
a       group A contains 'a', 'a', 'b', 'a', 'b'
a
b
a
b
a       group B contains 'a', 'b'
b

Sample Output
1 2 4
3 5

Explanation
'a' appeared 3 times in positions 1, 2 and 4.
'b' appeared 2 times in positions 3 and 5.
In the sample problem, if 'c' also appeared in word group , you would print -1.
"""
from collections import defaultdict
n=input().split()
grpa=n[0]
grpb=n[1]
# defaultdict(<class 'list'>, {'a': [1, 2, 4], 'b': [3, 5]})
d=defaultdict(list)
for i in range(int(grpa)):
    ch=input()
    d[ch].append(i+1)
print(d)
for j in range(int(grpb)):
    ch=input()
    if ch in d:
        print(*d[ch])
    else:
        print(-1)