class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
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