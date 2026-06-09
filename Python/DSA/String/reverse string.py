#way 1: reversed
s=input()  # s="Iswariya"
rev=reversed(s) # obj>>122993
print("".join(rev))
''' tc = O(n) because join() traverses all characters once..
sc = O(n) because join() creates a new reversed string of size n. '''
# ------------------------------------------

# way 2 : slicing
reve=s[::-1]
print("".join(reve))
'''tc = O(n) - slicing traverses all characters to create the reversed string.
 sc = O(n) - a new reversed string of size n is created. '''
# ------------------------------------------

# way 3 
reverse=""
for ch in s:
    reverse = ch+reverse
    # 1.b 2.a+b =ab, 3. c+ab=cab, 4. k+cab=kcab 
print(reverse)
'''tc = O(n²) - each string concatenation creates a new string and copies existing characters.
sc = O(n) - the final reversed string stores n characters.
'''
# ------------------------------------------

# way 4: 2 pointer
def str_rev(array):
    left=0
    right=len(s)-1
    while left<right:
        array[left],array[right]=array[right],array[left]
        left+=1
        right-=1
    return "".join(array)
print(str_rev(list(s)))
'''tc = O(n) - two-pointer swapping and join() each traverse the string once.
sc = O(n) - list(s) and the final joined string require extra memory.
'''  