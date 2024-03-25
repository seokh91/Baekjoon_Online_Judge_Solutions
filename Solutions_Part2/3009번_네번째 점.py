x_l=[]; y_l=[]
for _ in range(3):
    x,y=input().split()
    x_l.append(int(x)); y_l.append(int(y))

for i in range(3):
    if x_l.count(x_l[i]) == 1 : result_x=x_l[i]
for i in range(3):
    if y_l.count(y_l[i]) == 1 : result_y=y_l[i]

print(result_x, result_y)


    
