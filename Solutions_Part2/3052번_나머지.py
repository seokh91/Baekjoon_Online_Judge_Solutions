l=[]
for _ in range(42):
    l.append(0)
for _ in range(10):
    a=int(input())
    l[a%42]=1
print(l.count(1))
