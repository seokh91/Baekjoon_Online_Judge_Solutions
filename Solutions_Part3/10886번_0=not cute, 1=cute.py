n=int(input())
dic={0:0, 1:0}
for i in range(n):
    dic[int(input())]+=1

if dic[0] < dic[1] : print('Junhee is cute!')
elif dic[0] > dic[1] : print('Junhee is not cute!')
