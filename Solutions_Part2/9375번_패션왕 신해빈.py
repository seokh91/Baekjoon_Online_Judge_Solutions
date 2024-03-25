for _ in range(int(input())):
    cloth=dict()
    for _ in range(int(input())):
        _, temp=input().split()
        if temp in cloth : cloth[temp]+=1
        else : cloth[temp]=1
    res=1
    for i in list(cloth.values()):
        res*=(i+1)
    print(res-1)
