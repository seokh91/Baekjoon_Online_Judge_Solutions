import sys
s=set()
for _ in range(int(input())):
    line=sys.stdin.readline().split()
    line.append('0'); line[1]=int(line[1])

    if line[0]=='add': s.add(line[1])
    elif line[0]=='remove': s.discard(line[1])
    elif line[0]=='check':
        if line[1] in s: print(1)
        else : print(0)
    elif line[0]=='toggle':
        if line[1] in s : s.discard(line[1])
        else : s.add(line[1])
    elif line[0]=='all': s=set(range(1,21))
    elif line[0]=='empty': s.clear()
