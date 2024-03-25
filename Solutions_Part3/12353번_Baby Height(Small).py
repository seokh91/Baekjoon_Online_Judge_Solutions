from math import*
l=[]
n=int(input())
for _ in range(n):
    s,m,f=input().split()
    height=0
    temp_height=m.split("'"); temp_height[1]=temp_height[1].rstrip('"')
    height+=(12*int(temp_height[0])+int(temp_height[1]))
    temp_height=f.split("'"); temp_height[1]=temp_height[1].rstrip('"')
    height+=(12*int(temp_height[0])+int(temp_height[1]))
    if s=='B' : height += 5
    elif s=='G' : height -= 5
    l.append(height/2)

for i in range(n):
    min_=ceil(l[i]-4); max_=floor(l[i]+4)
    result_min=str(min_//12)+"'"+str(min_%12)+'"'
    result_max=str(max_//12)+"'"+str(max_%12)+'"'
    print('Case #%d: %s to %s'%(i+1, result_min, result_max))
