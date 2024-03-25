import sys
for _ in range(int(input())):
    a,b=sys.stdin.readline().split()
    result=0
    for i in b:result+=int(i)
    result%=(int(a)-1)
    print(result)
