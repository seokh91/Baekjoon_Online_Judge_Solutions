import sys
lines=[sys.stdin.readline().rstrip('\n') for _ in range(8)]
white=0
for i in range(8):
    if i%2==0:
        for j in range(0,8,2):
            if lines[i][j]=='F' : white+=1
    else :
        for j in range(1,8,2):
            if lines[i][j]=='F' : white+=1
print(white)
