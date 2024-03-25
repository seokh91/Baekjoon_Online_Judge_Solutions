import sys
n=int(input())
words=[list(sys.stdin.readline().split()) for _ in range(n)]

for i in words:
    temp=[]
    for j in range(len(i[0])):
        if ord(i[0][j]) <= ord(i[1][j]):
            temp.append(ord(i[1][j])-ord(i[0][j]))
        else:
            temp.append(ord(i[1][j])-ord(i[0][j])+26)
    print('Distances:', end=' ')
    for z in temp:
        print(z, end=' ')
    print()
