#with statement automatically do close()
with open("README.md") as f:
    print(f.read())

#r=read, t=text b=binary
d=open(r"C:\Users\ADMIN\Documents\assessment.txt", "rt")
print(d.readline())
print(d.readline(20))
# print(d.readlines())
d.close()
# print("\n") ---2line space
#single line space
print()  

with open("README.md") as file:
    for x in file:
        print(x)

# w=overwrite, a= append at end
with open("README.md", "w") as g:
    g.write("Practise Problem solving")

# File creation and deletion
    """
    h=open("myfile.txt","x")
    import os
    if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
    else:
    print("The file does not exist") 
    """
