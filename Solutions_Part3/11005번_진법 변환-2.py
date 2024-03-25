def trans(a,x):
    s=''
    while a>0:
        a,r=divmod(a,x)
        if(r>9):r=chr(ord('A')+r-10)
        s=str(r)+s
    return s
a,x=map(int, input().split())
print(trans(a,x))
