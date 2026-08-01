'''
june 28 — Easy

1.Given a string, return the count of vowels in it.
Input: "hello world"
Output: 3
'''
n=input()
counting=[ch for ch in n if ch in "aeiouAEIOU"]
print(len(counting))

# tc =o(n)  sc = o(n)