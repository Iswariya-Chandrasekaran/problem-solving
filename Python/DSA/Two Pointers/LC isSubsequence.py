class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sleft=0
        tleft=0
        while sleft < len(s) and tleft < len(t):
            if s[sleft]==t[tleft]:
                sleft+=1
                tleft+=1
            else:
                tleft+=1
        if sleft==len(s):
            return True
        return False

A=Solution()
print(A.isSubsequence("abc","ahbgdc"))
print(A.isSubsequence("axc","ahbgdc"))

""" 
https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=leetcode-75

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some
 (can be none) of the characters without disturbing the relative positions of the remaining characters. \
    (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
"""