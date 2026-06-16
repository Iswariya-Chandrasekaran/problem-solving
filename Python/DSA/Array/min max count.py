arr=[39,39,45,67,54,32,39,45]

cnt=[]

for i in range(len(arr)):
    x=arr.count(arr[i])
    cnt.append(x) # [3,3,2,1,1,1,3,2]
maxi=max(cnt) # 3
mini=min(cnt) # 1
y,z=cnt.index(maxi), cnt.index(mini) # y=0, z=3
print(arr[y],arr[z]) # 39, 67


# this is wrong since 67,54 and 32 all comes once out of that 32 is the min