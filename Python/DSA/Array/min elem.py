#--------------> Finding the minimum element in the array

arr = [8, 3, 11, 1, 7]
min=arr[0]
for i in range(len(arr)):
    if min > arr[i]:
        min=arr[i]
print(min)
# Expected output: 1

#---------->Fining the unique elements in the array
arr = [1, 2, 2, 3, 4, 4, 5]
unique=set(arr)
print(list(unique))
# Expected output: [1, 2, 3, 4, 5]

# Order preserved version
seen = set()
unique = []
for x in arr:
    if x not in seen:
        unique.append(x)
        seen.add(x)

#----------> Searching for an element in the array
def search(arr, target):
    if target in arr:
            return True
    return False