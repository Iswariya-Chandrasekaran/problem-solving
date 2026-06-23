s = "Hello, World Python  sorry"
y=s.split()
print(len(y))

'''tc= o(1) no operation, sc=o(n) new set'''
# in old code used set("aeiou")
# Set gives O(1) average lookup time since no dupliacte value direct lookup, 
# so it is better for frequent membership checks.
vowel="aeiou" 
count=0
'''tc=o(n) for loop, sc=o(1)''' 
for ch in s.lower(): 
    '''tc=o(n), sc = o(1)'''
    if ch in vowel: 
       count+=1
print(count)


