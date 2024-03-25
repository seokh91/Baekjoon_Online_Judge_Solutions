dic='abcdefghijklmnopqrstuvwxyz'
n=list(input())

for i in range(26):
    if dic[i] in n :
        print(n.index(dic[i]), end=' ')
    else:
        print(-1, end=' ')
