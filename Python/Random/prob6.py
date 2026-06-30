'''
Q3 — Medium
Given a string with only brackets ()[]{}, return True if it is valid (every open bracket 
has a matching closing bracket in correct order), else False.
Input: "()[]{}"
Output: True

Input: "([)]"
Output: False

Input: "{[]}"
Output: True
'''
brackets=input()
bracket_stack=[]
def fnbrackets(bracketstr):
    for ch in bracketstr:
        if ch in ["[", "{", "("]:
            bracket_stack.append(ch)
        elif ch in ["]", "}", ")"]:
            if not bracket_stack:
                return False
            last_open_brack=bracket_stack.pop()
            if last_open_brack=="{" and ch!="}":
                return False
            elif last_open_brack=="[" and ch!="]":
                return False
            if last_open_brack=="(" and ch!=")":
                return False

    return len(bracket_stack)==0

print(fnbrackets(brackets))

#tc = o(n) sc = o(n)