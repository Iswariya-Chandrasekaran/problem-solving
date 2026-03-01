# Function A
def is_palindrome_A(s):
    return s == s[::-1] #tc=o(n)internal looping ,sc=o(n) creates new string for comparing

# Function B - Two Pointer Approach
def is_palindrome_B(s):
    left = 0
    right = len(s) - 1  #c = o(n) for finding length
    while left < right: #tc=o(n)
        if s[left] != s[right]: # tc=o(1) since directly accessing and checking
            return False
        left += 1
        right -= 1
    return True

print(is_palindrome_A("racecar"))
print(is_palindrome_B("racecar"))



'''**Function A:**
TC = O(n) ✅ — internal loop to reverse
SC = O(n) ✅ — new reversed string created

**Function B:**
TC = O(n) ✅
SC = O(1) ✅ — just two pointer variables'''
