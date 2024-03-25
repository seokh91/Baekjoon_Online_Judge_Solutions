l=[]
def judge(c,n):
    al='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result_c=al.index(c[0])*(26**2)+al.index(c[1])*26+al.index(c[2])
    result_n=int(n)
    result_both=abs(result_c-result_n)
    if result_both < 100 : return 'nice'
    else : return 'not nice'
    
for _ in range(int(input())):
    l.append(input())
for i in l:
    print(judge(i[0:3],i[4:8]))
