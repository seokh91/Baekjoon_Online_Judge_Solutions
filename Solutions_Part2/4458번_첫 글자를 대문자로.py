import sys
low='qwertyuiopasdfghjklzxcvbnm'
upper='QWERTYUIOPASDFGHJKLZXCVBNM'

n=int(input())
l=[list(sys.stdin.readline()) for _ in range(n)]
for i in l:
    if i[0] in low:
        i[0]=upper[low.index(i[0])]

for i in l:
    temp_str=''
    for j in i:
        temp_str+=j
    print(temp_str, end='')
