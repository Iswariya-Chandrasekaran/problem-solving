# Q7. Write a function that checks if any two numbers in a sorted array add up to a given target.

class TwoSumIsTarget:
    def twosum(self,target:int,sortlist:list[int])->list[int]:
        left=0
        right=len(sortlist)-1
        while left < right:
            cur_sum=sortlist[left]+sortlist[right]
            if cur_sum==target:
                return left,right
            elif cur_sum < target:
                left+=1
            else:
                right-=1
        print("No Combination")
        return -1
A=TwoSumIsTarget()
result=A.twosum(10, [1,2,4,6,8,9,10] )
print(result)