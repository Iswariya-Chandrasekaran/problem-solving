"""
A word is defined as a sequence of non-space characters.
 The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Input: s = "   a good   example  "
Output: "example good a"
"""
class Solution(object):
    def reverseWords(self, s):

        arr=s.strip().split()
        rev_s=list(reversed(arr))
        print(" ".join(rev_s))
A=Solution()
A.reverseWords("the sky is blue")
        