# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(input())
M1=set(map(int,input().split()))
N = int(input())
N1=set(map(int,input().split()))
diff=M1.symmetric_difference(N1)
arr=list(diff)
arr.sort()
for x in arr:
    print(x)