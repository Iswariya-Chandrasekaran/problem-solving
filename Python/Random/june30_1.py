'''
Q1 — Easy
Given a list of numbers, find the second largest number in the list (without using sort() or sorted()).
Input: [10, 5, 8, 20, 3]
Output: 10
'''
mylist=list(map(int, input().split()))
if len(mylist) < 2:
    print("Not enough input")
def sec_large(arr):
    first_max=max(arr[0],arr[1])
    second_max=min(arr[0],arr[1])
    for i in range(2, len(arr)):
        if arr[i] > first_max:
            second_max=first_max
            first_max=arr[i]
        elif arr[i] > second_max:
            second_max=arr[i]
    return second_max
print(sec_large(mylist))