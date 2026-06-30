if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    if n>=2 and n<=10 and len(arr)==n:
            unique_list =sorted(set(arr))
            if len(unique_list)>=2:
                print(unique_list[-2])