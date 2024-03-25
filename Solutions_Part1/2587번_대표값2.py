import sys
data=[int(sys.stdin.readline()) for _ in range(5)]
data.sort()

aver=int(sum(data)/5)
median=data[2]

print(aver)
print(median)
