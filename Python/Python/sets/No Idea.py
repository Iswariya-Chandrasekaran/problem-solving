# a,b=map(int,input().split())
# arr=list(map(int,input().split()))
# A=set(map(int,input().split()))
# B=set(map(int,input().split()))
# like=0

# for ele in arr:
#     if ele in A:
#         like+=1
#     elif ele in B:
#         like-=1
# print(like)

#Optimised Way

a,b=map(int,input().split())
arr=list(map(int,input().split()))
A=set(map(int,input().split()))
B=set(map(int,input().split()))

print(sum((i in A)-(i in B) for i in arr))