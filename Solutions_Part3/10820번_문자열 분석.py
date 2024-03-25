import sys
l=[]
while 1:
    line=sys.stdin.readline().rstrip('\n')
    if not line : break
    l.append(line)
s='qwertyuiopasdfghjklzxcvbnm'
b='QWERTYUIOPASDFGHJKLZXCVBNM'
sp=' '

for i in l:
    cnt_s=0; cnt_b=0; cnt_sp=0; cnt_num=0
    for z in i:
        if z in s: cnt_s+=1
        elif z in b: cnt_b+=1
        elif z in sp: cnt_sp+=1
        else : cnt_num+=1
    print('%d %d %d %d'%(cnt_s,cnt_b,cnt_num,cnt_sp))
