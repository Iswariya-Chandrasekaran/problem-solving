# Enter your code here. Read input from STDIN. Print output to STDOUT
group_size=int(input()) #5
rooms=list(map(int,input().split())) # 1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2
no_dup=set(rooms) 
a=sum(rooms)
print(a) #113
b=sum(no_dup)*group_size 
print(b) #145
captain=(b-a)//(group_size-1) #8
print(captain)