# frequency of letters in both string same
# silent ==listen, rat==tar
# way 1 - Sorting both str
def anagram_check(str1,str2):
    if len(str1) != len(str2):
        return False
    s1_sorted=sorted(str1)  #['e', 'i', 'l', 'n', 's', 't']
    s2_sorted=sorted(str2)
    if s1_sorted == s2_sorted:
        return True
    return False

print(anagram_check("listen","silent"))
print(anagram_check("rat","rac"))

''' tc = O(n log n) not o(n) Because comparison-based sorting is not linear
sc=O(n) because sorted creates new list'''

#way 2: hash
s1="rat"
s2="tar"

def is_anagram(str1,str2):
    if len(str1) != len(str2):
        return False
    freq={}
    for ch in str1:
        freq[ch]=freq.get(ch,0)+1

    for ch in str2:
        freq[ch]=freq.get(ch,0)-1
    
    for val in freq.values():
        if val!=0:
            return False
    return True

print(is_anagram(s1,s2))

'''tc = O(n) since looping
sc = O(n) since creating a new dictionary
'''



