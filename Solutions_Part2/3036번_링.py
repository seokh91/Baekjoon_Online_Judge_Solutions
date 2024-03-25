n=int(input())
gcd=lambda a,b : a if not b else gcd(b, a%b)
t=list(map(int, input().split()))
for i in range(1, n):
    print("{}/{}".format(t[0]//gcd(t[0], t[i]), t[i]//gcd(t[0], t[i])))
