'''
july 7 — Easy-Medium
2. You are given a positive integer n. Return True if it is a perfect square, else False.
 Do not use math.sqrt().
Input:  16
Output: True

Input:  14
Output: False
'''
n=int(input())

def isperfectsquare(n):
    low=1
    high=n

    while low <= high:
        mid= (low+high) // 2  # 1+16 = 17 //2 = 8
        square = mid * mid  # 64
        if square == n:
            return True
        elif square < n:
            low=mid+1      
        else:
            high=mid-1  # high=8-1=7
    return False

print(isperfectsquare(n))

#tc = o(log n) sc = o(1)