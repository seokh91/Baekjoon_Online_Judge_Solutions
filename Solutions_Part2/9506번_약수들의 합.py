l=[]
while True:
    a=int(input())
    if a==-1: break
    l.append(a)

def judge_perfect(num):
    temp=[]; sumation=0
    for i in range(1,num):
        if num%i==0:
            temp.append(i)
            sumation+=i
    if sumation==num: return temp
    else: return 0

for i in range(len(l)):
    if judge_perfect(l[i])==0: print('%d is NOT perfect.'%l[i])
    else :
        print(l[i],'= ',end='')
        for j in range(len(judge_perfect(l[i]))-1):
            print(judge_perfect(l[i])[j],'+ ',end='')
        print(judge_perfect(l[i])[j+1])            
    
