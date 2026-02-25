#  Short cut Inverted pyramid

n=4
for i in range(1, n+1):
    print(" " * (i-1) + "*" * (2*(n - i) + 1))
    
# ----------------------- Number Pyramid-------

num=6
for i in range(1,num+1):
    for a in range(num-i):
        print(" ", end=" ")
    for b in range(2*i-1):
        print(i,end=" ")
    print()

# -------------------star pyramid without spaces bet'n stars

height=6
for i in range(1,height+1):
    for a in range(height-i):
        print(" ", end="")
    for b in range(2*i-1):
        print("*",end="")
    print()

# ----------------------REVERSE sequence NUMBER PYRAMID-------

n=6
for i in range(1,n+1):
    for a in range(i-1):
        print(" ", end=" ")
    for b in range(1,2*(n-i)+2):
        print(b,end=" ")
    print()

# ----------------------- Reverse Number Pyramid-------

num=6
for i in range(1,num+1):
    for a in range(i-1):
        print(" ", end=" ")
    for b in range(2*(num-i)+1):
        print(num-i+1,end=" ")
    print()

