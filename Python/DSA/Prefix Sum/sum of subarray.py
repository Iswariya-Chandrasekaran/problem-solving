my_list=[1, 3, 5, 7, 9]

def build_prefix(arr):
    prefix=[0]*len(arr) #[0,0,0,0]              o(n)
    prefix[0]=arr[0] #prefix[0]=[2]
    for i in range(1,len(arr)):
        # prefix[1]= prefix[1-1]+arr[1] --> 2+5=7
        # prefix[2]=prefix[2-1]+arr[2] --> 7+89
        prefix[i]=prefix[i-1]+arr[i]  
    return prefix
x= build_prefix(my_list) #[2, 7, 94, 179]

def range_sum(prefix_list,L,R):
    if L==0:
        return prefix_list[R]
    return prefix_list[R]-prefix_list[L-1]

print(range_sum(x,0,2))
print(range_sum(x,1,4))
print(range_sum(x,2,3))