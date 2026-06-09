nums=[1,2,43,2,1]
freq = {}

for num in nums:
    # First item (1): 1 is not in freq. so freq.get(1, 0) returns 0. Add 1. freq[1] becomes 1.
    # Second item (2): 2 is not in freq. so freq.get(2, 0) returns 0. Add 1. freq[2] becomes 1.
    # Fourth item (2): 2 is in freq. so freq.get(2, 0) returns 1. Add 1+1. freq[2] becomes 2.
    freq[num] = freq.get(num, 0) + 1
    
print(freq)