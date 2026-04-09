class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
      Merge two strings alternately. 
        Example:
        word1 = "abc"  word2 = "pqr"
        Output = "apbqcr"
        """
        # 1. Initialise empty string
        a=""
        # 2. initialise index pointer
        i=0
        # 3. Loop untill both strings are fully traversed
        while i < len(word1) or i < len(word2):
            # 4. Add char from word1 if index is valid
            if i < len(word1):
                a = a+word1[i]
            # 5. Add char from word2 if index is valid
            if i < len(word2):
                a = a+word2[i]
            # 6. Move to next index
            i=i+1 
        # Return final string    
        return a

A=Solution()
result=A.mergeAlternately("abc","pqr")
print(result)

""" https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75"""