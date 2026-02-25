# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

A=list(map(int, input().split()))  #[1,2]
B=list(map(int, input().split())) #[3,4]
C=list(product(A,B))

for x in C:
    print(x,end=" ") #(1, 3) (1, 4) (2, 3) (2, 4)
    

