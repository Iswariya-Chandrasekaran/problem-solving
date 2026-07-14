'''
Q2 — Easy-Medium
You are given a sorted list of integers and a target. Return True if any two numbers
 in the list add up to the target, else False. Do not use a HashMap — use two pointers.
Input:  nums = [1, 2, 3, 4, 6], target = 6
Output: True   # 2 + 4 = 6
Input:  nums = [1, 2, 3, 4, 6], target = 20
Output: False
'''
arr=list(map(int,input().split()))
target=int(input())
def pointertarget(arr,target):
    left=0
    right=len(arr)-1
    while left < right:
        if arr[left]+arr[right] < target:
            left+=1
        elif arr[left]+arr[right] > target:
            right-=1
        else:
            return True
    return False
print(pointertarget(arr,target))
