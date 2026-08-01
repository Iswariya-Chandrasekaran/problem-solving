'''
july 6 — Easy-Medium
2. You are given two positive integers. Find their GCD (Greatest Common Divisor) - the largest 
number that divides both without a remainder. Do not use math.gcd().
Input:  48, 18
Output: 6

Input:  100, 75
Output: 25
'''
a = int(input())
b = int(input())

while b:
    a, b = b, a%b
print(a)

# tc= o(n) sc=o(1)