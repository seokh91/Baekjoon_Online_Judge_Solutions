import sys
l=[list(sys.stdin.readline().rstrip('\n')) for _ in range(5)]
max_length=len(l[0])
for i in l :
    if max_length < len(i) : max_length=len(i)
for i in range(5) :
    if max_length > len(l[i]) :
        for _ in range(max_length-len(l[i])) : l[i].append('@')
result=''
for i in range(max_length):
    for j in range(5):
        if l[j][i] == '@' : result+=''
        elif l[j][i] != '@' : result+=l[j][i]
print(result)
