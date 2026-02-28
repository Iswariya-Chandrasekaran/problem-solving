# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
AB= int(input())
BC=int(input())
radian=math.atan(AB/BC) #atan means tan inverse
theta=round(math.degrees(radian))
print(f"{theta}\u00b0") #u00b0 is the unicode method for °