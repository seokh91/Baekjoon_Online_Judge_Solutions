n=int(input())
l_0=[]
for _ in range(n):
    l_1=[]
    a,b=input().split()
    a=int(a); b=int(b)
    for _ in range(b):
        l_1.append(0)
    for _ in range(a):
        c=int(input())
        l_1[c-1] += 1
    l_0.append(l_1)

for i in l_0:
    result=0
    for j in i:
        if j > 1 : result+=j-1
    print(result)
