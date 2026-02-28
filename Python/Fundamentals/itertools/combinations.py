from itertools import combinations

S,K=input().split() 
# S= BCAD , K= 3
s=sorted(S) # s=ABCD
k=int(K)
for i in range(1,k+1):
    comb=list(combinations(s,i))
    for x in comb:
        print("".join(x))

""" O/P
A
B
C
D
AB
AC
AD
BC
BD
CD
ABC
ABD
ACD
BCD

"""