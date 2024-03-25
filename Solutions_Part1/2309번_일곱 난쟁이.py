import sys
high=[int(sys.stdin.readline()) for _ in range(9)]
high.sort()
for i in range(8):
    for j in range(i+1, 9):
        if sum(high)-high[i]-high[j]==100:
            high[i]=0; high[j]=0
            break
for i in high:
    if i != 0:print(i)
