import sys
get=sys.stdin.readline().rstrip('\n')

def check(get):
    temp_stack=[]
    for i in get :
        if i=='(' or i=='[':temp_stack.append(i)
        elif i==')' or i==']':
            temp=temp_stack[len(temp_stack)-1]
            if (i+temp)==')(' or (i+temp)=='][' : temp_stack.pop(len(temp_stack)-1)
            else : break
    if temp_stack == [] : return True
    else : return False

if check(get) :
    get=get.replace('()','2'); get=get.replace('[]','3')
    stack=[]
    for i in range(len(get)):
        temp=0
        if get[i]==')' :
            temp_index=len(stack)-1
            while stack[temp_index] != '(' :
                temp+=int(stack[temp_index])
                stack.pop()
                temp_index-=1
            stack.pop()
            stack.append(2*temp)
            
        elif get[i]==']' :
            temp_index=len(stack)-1
            while stack[temp_index] != '[' :
                temp+=int(stack[temp_index])
                stack.pop()
                temp_index-=1
            stack.pop()
            stack.append(3*temp)

        else : stack.append(get[i])
    stack=list(map(int, stack))
    print(sum(stack))              

elif not check(get) : print(0)
