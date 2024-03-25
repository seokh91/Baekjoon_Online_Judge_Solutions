import sys
num=sys.stdin.readline().rstrip('\n')
len_num=len(num) ; num=int(num)

flag=False ; temp=0

if num-len_num*9 < 0 : temp=-1

for i in range(num-(len_num+temp)*9, num):
    if i+sum(map(int, list(str(i)))) == num :
        flag=True
        print(i)
        break

if not flag : print(0)
