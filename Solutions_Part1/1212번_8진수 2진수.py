n=input(); result=''; temp=len(n)
l=['000','001','010','011','100','101','110','111']

for i in range(temp):
    if i==0:
        if n[0]=='0':print('0')
        elif n[0]=='1':print('1',end='')
        elif n[0]=='2':print('10',end='')
        elif n[0]=='3':print('11',end='')
        else:print(l[int(n[i])],end='')
    else:
        print(l[int(n[i])],end='')
