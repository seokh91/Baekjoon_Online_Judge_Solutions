import sys
import math as m

n=int(sys.stdin.readline().rstrip()) ; nums=[]
for _ in range(n):
    nums.append(int(sys.stdin.readline().rstrip()))
tmp=[] ; nums.sort()
gcd=lambda a,b : a if not b else gcd(b, a%b)

for i in range(len(nums)-1):
    tmp.append(nums[i+1]-nums[i])

if n==2:
    ms=nums[1]-nums[0]
else:
    ms=gcd(tmp[0], tmp[1])
    for i in range(2, len(tmp)):
        ms=gcd(ms, tmp[i])

tmp=set()
for i in range(2, int(m.sqrt(ms))+1):
    if ms%i==0 :
        tmp.add(i) ; tmp.add(ms//i)
        
tmp=[str(i) for i in sorted(list(tmp)+[ms])]
print(' '.join(tmp))
