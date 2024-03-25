l=[0,0,0,0,0,0,0,0,0,0]
a=int(input()); b=int(input()); c=int(input())
abc=a*b*c
abc=list(str(abc))

for i in range(len(abc)):
    l[int(abc[i])] += 1

for i in range(len(l)):
    print(l[i])
