a,b=list(map(int, input().split()))
gcd=lambda x,y : x if not y else gcd(y, x%y)
print(a*b//gcd(a,b))
