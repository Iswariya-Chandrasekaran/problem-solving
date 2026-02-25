from itertools import product

def maxi(X):
    return X*X

K,M= input().split()
lists=[]
S=[]
for i in range(int(K)):
    my_list=list(map(int,input().split()))
    lists.append(my_list)
    
combination=list(product(*lists))

for a in combination:
    add=[]
    for b in a:
        add.append(maxi(b))
    S.append(sum(add)%int(M))
print(max(S))