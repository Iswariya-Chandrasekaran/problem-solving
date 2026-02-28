# Enter your code here. Read input from STDIN. Print output to STDOUT
N=int(input())
my_set=set()

for i in range(N):
    x= input()
    my_set.add(x)
    
print(len(my_set))