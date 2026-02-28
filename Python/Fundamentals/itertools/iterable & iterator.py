from itertools import combinations

N=int(input())
my_list=list(input().split())
K=int(input())

x=list(combinations(my_list,K))
den=len(x)
count=0

for i in x:
    if my_list[K-1] in i:
        count+=1
prob=count/den
print(f"{prob:.3f}")