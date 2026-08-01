'''
june 30 — Easy-Medium
2. Given a list of numbers, move all zeros to the end while keeping the relative order
 of non-zero elements. Do it in-place if possible.
Input: [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]
'''
mylist=list(map(int, input().split()))
# for i in range(len(mylist)):
#     if mylist[i]==0:
#         mylist.remove(0)
#         mylist.append(0)
# print(mylist)

pos=0
for i in range(len(mylist)):
    if mylist[i]!=0: #i=1: 1, i=3: 3 i=4: 12
        mylist[pos],mylist[i] = mylist[i],mylist[pos] #[1,0,0,3,12], [1,3,0,0,12], [1,3,12,0,0]
        pos+=1 # pos=1,2
print(mylist)  
