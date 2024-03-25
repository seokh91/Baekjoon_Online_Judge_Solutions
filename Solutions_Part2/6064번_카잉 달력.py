import sys

def get_lcm(a,b):
    gcd=lambda a,b : a if not b else gcd(b, a%b)
    lcm=int(a*b/gcd(a,b))
    return lcm

temp=lambda a,b,c : (a+b)%c if (a+b)%c!=0 else c
temp_1=lambda a,b : a%b if a%b!=0 else b

for _ in range(int(input())):
    m,n,x,y=map(int, sys.stdin.readline().rstrip('\n').split())

    lcm=get_lcm(m,n) ; a=x ; b=y ; judge=False

    if m>n : b=temp_1(a,n) ; cnt=a ; big=m ; d=m-n
    else : a=temp_1(b,m) ; cnt=b ; big=n ; judge=True ; d=n-m

    while True :
        if cnt > lcm : print(-1) ; break
        else :
            if a==x and b==y : print(cnt) ; break
            else :
               cnt+=big
               if not judge : b=temp(b,d,n) 
               else : a=temp(a,d,m)
