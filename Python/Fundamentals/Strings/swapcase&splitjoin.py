def swap_case(s):  
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

# First it'll ask swapcase input then gives output and 
# then it'll ask split and join input and gives output


def split_and_join(line):
    splitline=line.split(" ")
    joinline="-".join(splitline)
    return joinline
    # write your code here

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
