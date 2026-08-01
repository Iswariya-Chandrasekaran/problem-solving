'''
July 1 — List Intersection
3 Given two lists of integers, return a new list containing only the elements that appear in both lists. 
The result should not contain duplicates even if the element appears multiple times in both lists.
Input:  a = [1, 2, 2, 3, 4],  b = [2, 2, 3, 5]
Output: [2, 3]
Input:  a = [1, 5, 7, 9],  b = [5, 9, 10]
Output: [5, 9]
'''
alist=list(map(int,input().split()))
blist=list(map(int,input().split()))
aunique=set(alist)
bunique=set(blist)
print(list(aunique & bunique))