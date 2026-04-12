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
        