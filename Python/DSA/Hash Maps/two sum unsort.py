nums = [2,7,11,15]
target = 10

def two_sum(nums,target):
    lookup = {}
    for i, num in enumerate(nums):
        needed = target - num
        
        if needed in lookup:
            return [lookup[needed], i]
        
        lookup[num] = i
print(two_sum(nums,target))