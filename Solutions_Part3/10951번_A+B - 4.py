import sys
l=[]
while True:
    line=sys.stdin.readline().rstrip('\n')
    if line=='': break
    l.append(sum(list(map(int, line.split()))))

for i in l:
    print(i)
