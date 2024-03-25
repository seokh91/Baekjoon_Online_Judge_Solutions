import sys
l=[]
while True:
    line=sys.stdin.readline().rstrip('\n')
    if not line:
        break
    l.append(line)

for i in l:
    print(i)
