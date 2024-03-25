x,y=input().split()
x=list(x); y=list(y)

def Rev(list_):
    temp=[]; result=''
    for i in range(1, len(list_)+1):
        temp.append(list_[-i])
    for i in temp:
        result+=i
    return int(result)

print(Rev(list(str(Rev(x)+Rev(y)))))
