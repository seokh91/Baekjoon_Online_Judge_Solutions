import sys
n=int(input())
score=[tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
avrg=[]

for i in score:
    avrg.append(sum(i[1:])/i[0])
for i in range(n):
    cnt=0
    for j in range(1, score[i][0]+1):
        if avrg[i] < float(score[i][j]):
            cnt+=1
    print('%.3f'%((cnt/score[i][0])*100),end='%\n')
