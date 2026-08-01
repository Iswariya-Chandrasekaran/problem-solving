'''
july 6 — Easy
1. You are given a positive integer n. Return True if it is a prime number, else False.
 A prime number is divisible only by 1 and itself.
Input:  7
Output: True

Input:  12
Output: False
'''
n=int(input())

def isprime(n):
    count=0
    for i in range(1,n+1):
        if n % i == 0:
            count+=1
    if count == 2:
        return False
    return True

print(isprime(n))

# tc= o(n) sc=o(1)