def average(array):
    distinct=set(array)
    total=sum(distinct)
    a=len(distinct)
    p=total/a
    return f"{p:.3f}"
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)