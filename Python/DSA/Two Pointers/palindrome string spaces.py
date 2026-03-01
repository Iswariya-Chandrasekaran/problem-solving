"""
**Q8.** This is a TCS NQT style question:
```
Given a string, check if it is a palindrome 
IGNORING spaces and special characters.

Example 1: "A man a plan a canal Panama"  → True
Example 2: "hello world"                  → False
Example 3: "Was it a car or a cat I saw"  → True

"""
class solution:
    def is_palindrome(self,s:str)->str:
        s=s.strip()
        s=s.lower()
        s="".join(ch for ch in s if ch.isalnum())
        left=0
        right=len(s)-1
        while left < right:
            if s[left] != s[right]:
                 return False  
            left+=1
            right-=1 
        return True
string1=solution()
print(string1.is_palindrome("A man !   a plan a #canal Panama)"))