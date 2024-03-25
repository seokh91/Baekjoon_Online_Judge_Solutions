a=list(input())
b=list(input())

for i in range(len(a)):
    if a[i] in b :
        b[b.index(a[i])]='0'
        a[i]='0'
cnt_a=a.count('0'); cnt_b=b.count('0')        
print(len(a)+len(b)-cnt_a-cnt_b)
