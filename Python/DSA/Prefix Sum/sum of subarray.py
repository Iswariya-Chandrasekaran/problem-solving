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

def range_sum(arr1,L,R):
    if L==0:
        return arr1[R]
    return arr1[R]-arr1[L-1]

print(range_sum(x,0,2))
print(range_sum(x,1,4))
print(range_sum(x,2,3))