import sys
dic={1:[1], 2:[2,4,8,6], 3:[3,9,7,1], 4:[4,6], 5:[5], 6:[6], 7:[7,9,3,1], 8:[8,4,2,6], 9:[9,1], 0:[10]}
n=int(input())
l=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
for i in l:
    i[0]%=10

for i in l:
    index=i[1]%len(dic[i[0]])
    print(dic[i[0]][index-1])
