import sys
line=list(map(int, sys.stdin.readline().split()))
word=sys.stdin.readline().rstrip('\n')
dic={}; line.sort(); temp='ABC'
for i in range(3):
    dic.setdefault(temp[i], line[i])
for i in word:
    print(dic[i], end=' ')
