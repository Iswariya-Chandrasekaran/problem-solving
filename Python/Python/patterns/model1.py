# rows=4
# for i in range(rows): 
#     print("#", end=" ")
#     for j in range(rows-1):
#         print("$", end=" ")
#     print("#")

#--------------------------- right triangle-----------------------

height=4
for i in range(height): 
    for j in range(i+1):
        print("$", end=" ")
    print( )

# 2 --------------- 

rows=4
for i in range(1,rows+1): 
    for j in range(1,i+1):
        print("*", end=" ")
    print( )

# ----------------reverse triangle

height=4
for i in range(1,height+1): 
    for j in range(height-i+1):
        print("%", end=" ")
    print( )

# number pattern
num=4
for i in  range(1,num+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
       