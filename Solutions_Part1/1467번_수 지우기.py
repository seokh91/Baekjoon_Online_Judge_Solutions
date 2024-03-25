from collections import*
C=Counter; r=input()
a=r(); u=C(a)-C(r()); s=''; z=0
while u :d=chr(57-z);i=a.find(d);f=-1<i!=C(d)-u==u-C(a[i:]);s+=f*d;u-=C(f*d);a=a[-~i*f:]; z=~z*~-f
r(s)
