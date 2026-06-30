# Second largest number in an array without sorting

# arr=list(map(int, input().split()))
arr=[13,9,60,54,9,10]

def second_largest(arr):
    first=max(arr[0],arr[1]) # max(13,9)=13
    second=min(arr[0],arr[1]) #min(13,9)=9
    for i in range(2,len(arr)):
        if arr[i] > first: #60>13
            # primarily we should update second interger then only second
            second=first #second=13 
            first=arr[i] #first=60 
        elif arr[i] > second and arr[i]!=first:#6>9
            second=arr[i]
    return second
print(second_largest(arr))

arr=[13,9,60,60,54,9,10]
unique=list(set(arr))  #[9, 10, 13, 54, 60]
unique.sort(reverse=True) # [60,54,14,]
print(unique[1])

arry = [5,8,2,9,1,9,10]
print(sorted(set(arry))[-2])


