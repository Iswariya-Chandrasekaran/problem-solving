'''
july 6 — Medium
3 You are given a positive integer n. Return a list of all prime numbers up to and including n.
 This is called the Sieve of Eratosthenes.
Input:  20
Output: [2, 3, 5, 7, 11, 13, 17, 19]

Input:  10
Output: [2, 3, 5, 7]
''' 
n=int(input())
result=[]
for i in range(2,n+1):
    count=0
    for j in range(1,i+1):
        if i % j == 0:
            count+=1
    if count == 2:
        result.append(i)
print(result)

# tc= o(n*n) sc=o(n)
