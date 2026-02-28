# A=set(map(int,input().split()))
# N=int(input())
# arr=[]
# for i in range(N):
#     B=set(map(int,input().split()))
#     arr.append(A.issuperset(B))
# if False in arr:
#     print("False")
# else:
#     print("True")

#  ---------Optimized Way--------------

# A=set(map(int,input().split()))
# N=int(input())
# print(
#     all(A.issuperset(set(map(int,input().split()))) for i in range(N))
#     )

A=set(map(int,input().split()))
N=int(input())
for i in range(N):
    B=set(map(int,input().split()))
    if not A.issuperset(B):
        print("False")
        break
    else:
        print("True")


# A=set(map(int,input().split()))
# N=int(input())
# arr=[]
# for i in range(N):
#     B=set(map(int,input().split()))
#     arr.append(A.issuperset(B))
# if False in arr:
#     print("False")
# else:
#     print("True")

#  ---------Optimized Way--------------

# A=set(map(int,input().split()))
# N=int(input())
# print(
#     all(A.issuperset(set(map(int,input().split()))) for i in range(N))
#     )

A=set(map(int,input().split()))
N=int(input())
for i in range(N):
    B=set(map(int,input().split()))
    if not A.issuperset(B):
        print("False")
        break
    else:
        print("True")


