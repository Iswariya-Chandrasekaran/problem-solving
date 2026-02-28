# Enter your code here. Read input from STDIN. Print output to STDOU
# n=int(input())
# my_set=set(map(int,input().split()))

# for i in range(n):
#     cmd=input().split()
#     if cmd[0]=="pop":
#         my_set.pop()
#     if cmd[0]=="discard":
#         my_set.discard(int(cmd[1]))
#     if cmd[0]=="remove":
#         my_set.remove(int(cmd[1]))
        
# print(sum(my_set))


# Enter your code here. Read input from STDIN. Print output to STDOUT
# en=int(input())
# en_std=set(map(int,input().split()))
# fr=int(input())
# fr_std=set(map(int,input().split()))

# both=en_std & fr_std
# print(len(both))

test_case=int(input())
res=[]
for i in range(test_case):
    A=int(input())
    Aset=set(map(int,input().split()))
    B=int(input())
    Bset=set(map(int,input().split()))
    y=Aset.issubset(Bset)
    res.append(y)
for x in res:
 print(x)
