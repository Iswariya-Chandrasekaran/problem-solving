#  instead of creating all values at once and storing them in memory, 
#   it produces one value at a time, only when you ask for it.(Kitchen Dosa order)
def intro():
    try:
        yield "Hey"
        yield "Im Ishu"
        yield 21
    finally:
        print("Generator closed")

# -----------WRONG-----------
# → creates new generator object #1 , will vanish ag=fter hitting Hey
print(next(intro()))
print(next(intro())) # cretes new gen object 2 again, again hit Hey
# ------------------------------

# gen remembers where it paused. So every next(gen) 
#   continues from the last pause point.
# → generator object created. nothing runs yet.
gen=intro()
# → function starts running pauses after hitting Hey
print(next(gen)) 
# gen object again runs from where it stopped and hits Im Ishu
print(next(gen))
print(next(gen))
# Below raises: StopIteration  ← no more values left
# print(next(gen))
gen.close()

# generator can only be used once.But we can create new generator
new_gen=intro()
print(next(new_gen))

def num_produ(num):
    for i in range(1,num+1):
        yield i

gene=num_produ(3)
print(f"{next(gene)} is the first num ") #1 is the first num 
print(next(gene)) # 2
print(next(gene)+10) # 13

# or loop through this
for num in num_produ(3):
    print(num)
# 1
# 2
# 3

sqr_prod=(num*num for num in range(10))
print(next(sqr_prod)) # 0
print(next(sqr_prod)) # 1
print(next(sqr_prod)) # 4
print(next(sqr_prod)) # 9
# prints remaining yield in list
print(list(sqr_prod)) #[16, 25, 36, 49, 64, 81]
# print(sum(sqr_prod)) #271

