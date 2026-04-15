"""
A word is defined as a sequence of non-space characters.
 The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Input: s = "   a good   example  "
Output: "example good a"
"""
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr=s.split(" ")
        remo_space=[i for i in arr if i]
        rev_s=remo_space[::-1]
        print(" ".join(rev_s))
A=Solution()
A.reverseWords("the sky is blue")
        