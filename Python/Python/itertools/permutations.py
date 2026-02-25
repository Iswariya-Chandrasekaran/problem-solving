from itertools import permutations

S=input().split() # HACK 2
C=sorted(list(permutations(S[0],int(S[1])))) 
#[('A', 'C'), ('A', 'H'), ('A', 'K'), ('C', 'A'), ('C', 'H'), 
#      ('C', 'K'), ('H', 'A'), ('H', 'C'), ('H', 'K'), ('K', 'A'), ('K', 'C'), ('K', 'H')]
for x in C:
    print("".join(x))


""" O/P

AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH 

"""