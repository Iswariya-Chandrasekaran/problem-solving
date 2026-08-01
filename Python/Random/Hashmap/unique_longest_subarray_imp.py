'''
july 4 — Medium
3. You are given a list of integers. Find the length of the longest subarray where all 
elements are unique (no duplicates).
Input:  [1, 2, 3, 1, 2, 3, 4]
Output: 4   # subarray [1, 2, 3, 4] or [3, 1, 2, 3] -- wait:
            # [1, 2, 3, 4] → all unique ✅ length 4
Input:  [1, 1, 1, 1]
Output: 1
'''
given=list(map(int,input().split()))

seen=set()
wind_start=0
wind_end = 0
max_length=0

while wind_end < len(given):
    if given[wind_end] not in seen:
        seen.add(given[wind_end])
        current_wind_size = wind_end-wind_start+1
        max_length=max(max_length,current_wind_size)
        wind_end+=1
    else:
        seen.remove(given[wind_start])
        wind_start+=1

print(max_length)

#tc = o(n) sc=o(n)

# given = list(map(int, input().split()))

# seen = set()
# left = 0          # Tracks the start of the current unique subarray
# max_length = 0    # Tracks the longest length found so far

# # Loop through the array using 'right' as the end of the window
# for right in range(len(given)):
#     current_num = given[right]
    
#     # If we hit a duplicate, shrink the window from the left 
#     # until the duplicate element is removed from our set
#     while current_num in seen:
#         seen.remove(given[left])
#         left += 1  # Slide the left wall forward
        
#     # Now it's safe to add the current number to our unique window
#     seen.add(current_num)
    
#     # Calculate the size of the current window and update max_length
#     current_window_size = right - left + 1
#     max_length = max(max_length, current_window_size)

# print(max_length)
