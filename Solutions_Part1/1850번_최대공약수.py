import sys
l=list(map(int, sys.stdin.readline().split()))
l.sort()
gcd=lambda a,b : a if not b else gcd(b, a%b)
for i in range(gcd(l[0],l[1])):
    print(1, end='')
