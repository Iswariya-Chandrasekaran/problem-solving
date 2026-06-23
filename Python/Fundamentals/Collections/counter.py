# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter
X=int(input()) #10
shoe_sizes=list(map(int, input().split())) #[2, 3, 4, 5, 6, 8, 7, 6, 5, 18]
N=int(input()) # 6 

stock=Counter(shoe_sizes) #{5: 2, 6: 2, 2: 1, 3: 1, 4: 1, 8: 1, 7: 1, 18: 1}
price=0
for i in range(N):  
    size, rate = map(int, input().split())
    if size in stock and stock[size] >0:
        price=price+rate
        stock[size]-=1
print(price)  # 200

'''
Sample Input
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50

Sample Output: 200

Explanation

Customer 1: Purchased size 6 shoe for $55.
Customer 2: Purchased size 6 shoe for $45.
Customer 3: Size 6 no longer available, so no purchase.
Customer 4: Purchased size 4 shoe for $40.
Customer 5: Purchased size 18 shoe for $60.
Customer 6: Size 10 not available, so no purchase.

Total money earned = 200
'''