class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        left=0
        right=0
        while left < len(s) and right < len(t):
            if s[left]==t[right]:
                left+=1
                right+=1
            else:
                right+=1
        if left==len(s):
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