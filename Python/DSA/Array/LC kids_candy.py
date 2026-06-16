class extraCandy:
    """
    Determine which kids can have the greatest number of candies
    after adding extra candies.

    Example:
    candies = [2, 3, 5, 1, 3]
    extra = 3 max of arr is so 2+3=5 True, 3+3=6 True
    Output = [True, True, True, False, True]
    """
    def sum_count(self, candies:list[int], extra:int)-> list[bool]:
        # 1. Initialise empty result list
        result=[]
        # 2. Find the maximum number of candies in the list
        maxi=max(candies)
        # 3. Loop through each kid's candies and check if adding extra makes
        #  it greater than or equal to the maximum
        for i in range(len(candies)):
            sum = candies[i]+extra
            # 4. Append True to result if sum is greater than or equal to max
            if sum >= maxi:
                result.append(True)
            # 5.  else append False
            else:
                result.append(False)
        # 6. Return the result list
        return result

A= extraCandy()
print(A.sum_count([2,3,5,1,3], 3))