# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath
z=complex(input())
print(f"{abs(z):.3f}") # here r can be find via abs function = sqrt(x*x + y*y)
phi = cmath.phase(z)
print(f"{phi:.3f}")
# here phi can be find via phase function = atan(y/x)