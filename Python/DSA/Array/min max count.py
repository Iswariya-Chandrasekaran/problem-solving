arr=[39,39,45,67,54,32,39,45]

cnt=[]

for i in range(len(arr)):
    x=arr.count(arr[i])
    cnt.append(x)
maxi=max(cnt)
mini=min(cnt) 
y,z=cnt.index(maxi), cnt.index(mini)
print(arr[y],arr[z])