from itertools import groupby
S=input()

for key,group in groupby(S):
    x=list(group).count(key),int(key)
    print(x,end=" ")