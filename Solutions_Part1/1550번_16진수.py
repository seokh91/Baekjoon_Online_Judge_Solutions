import sys
line=list(sys.stdin.readline().rstrip('\n'))
line_0=[]
for _ in range(len(line)):
    line_0+=[line.pop()]
result=0; x='0123456789ABCDEF'

for i in range(len(line_0)):
    temp=1
    for _ in range(i): temp*=16
    result+=(temp*x.index(line_0[i]))

print(result)
