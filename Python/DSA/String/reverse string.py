# *"Reverse in place"*

s="Iswariya"
# ["I","s","w","a","r","i","y","a"]
mylist=list(s) #tc=o(n) for creating list, sc=o(n) for creating new list
def reverse_array(arr):
    left=0
    '''#o(n) for finding length'''
    right=len(arr)-1 # right=7  
    '''tc=o(n)'''
    while left<right: # 0<7, 1<6 
        # ["a","s","w","a","r","i","y","I"]
        # ["a","y","w","a","r","i","s","I"]
        arr[left],arr[right] = arr[right],arr[left] 
        left+=1 #l=1
        right-=1 #r=6
    return arr

rev_list=reverse_array(mylist)
'''tc=o(n) for join'''
rev_string="".join(rev_list)
print(rev_string)

''' tc = o(n),sc = o(n)'''