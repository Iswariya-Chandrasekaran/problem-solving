nums=[1,2,43,2,1]
freq = {}

for num in nums:
    freq[num] = freq.get(num, 0) + 1
    print(freq[num])