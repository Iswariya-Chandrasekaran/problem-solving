#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    x=s.split(" ")
    #  -------------will work only for 2 words of name---------------
    # name1=x[0].capitalize()
    # name2=x[1].capitalize()
    # x=f"{name1} {name2}"
    # return x
    name=[]
    for i in x:   
       name.append(i.capitalize())
       fullname=" ".join(name)
    return fullname

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

