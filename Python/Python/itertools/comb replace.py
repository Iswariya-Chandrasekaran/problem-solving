# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

S=input().split()  # BCAD 2
rep=list(combinations_with_replacement(sorted(S[0]),int(S[1])))
for x in rep:
    print("".join(x))

""" O/P
AA
AB
AC
AD
BB
BC
BD
CC
CD
DD
"""