import sys
n=int(input())
price=[sys.stdin.readline() for _ in range(n)]

price=list(map(float, price))
for i in range(n):
    price[i]=0.8*price[i]
for i in price:
    print('$%.2f' % i)
