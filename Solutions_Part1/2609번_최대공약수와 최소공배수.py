a,b=input().split()
a=int(a); b=int(b)

gcd=lambda a,b : a if not b else gcd(b, a%b)
gcd_1=gcd(a,b)
lcm=int((a*b)/gcd_1)

print(gcd_1)
print(lcm)
