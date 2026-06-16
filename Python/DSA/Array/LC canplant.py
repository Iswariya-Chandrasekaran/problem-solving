class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
Given an integer array flowerbed containing 0's and 1's, where 0 means empty 
and 1 means not empty, and an integer n, return true if n new flowers can 
be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
        """
        i=0
        count=0
        length=len(flowerbed)
        while i < length:
            if i==0:
                if flowerbed[i]==0 and (length==1 or flowerbed[i+1]==0):
                    count+=1
                    flowerbed[i]=1
            elif i<length-1:
                if flowerbed[i-1]==0 and flowerbed[i]==0 and flowerbed[i+1]==0:
                    count+=1
                    flowerbed[i]=1
            else:
                if flowerbed[i]==0 and flowerbed[i-1]==0:
                    count+=1
                    flowerbed[i]=1
            i+=1
        if count >= n:
            return True
        else:
            return False
A= Solution()
print(A.canPlaceFlowers([0,0,1,0,0],1))

''' https://leetcode.com/problems/can-place-flowers/?envType=study-plan-v2&envId=leetcode-75 '''