import sys
N=input()
K=list(input())
result_list=[]

for i in K:

    '''if i not in N :
        result_list.append(N)
        continue'''

    if N.count(i)==1:
        N=list(N.replace(i, 'a'))
        N.remove('a')
        result=''
        for j in N : result+=j
        N=result
        result_list.append(N)
        #print(N)

    elif N.count(i)!=1 :
        
        criter_index=N.find(i)
        while criter_index+2*len(i)<=len(N):
            
            temp_int=int(N[criter_index:criter_index+len(i)])
            temp_int_1=int(N[criter_index+len(i):criter_index+len(i)+len(i)])

            if temp_int < temp_int_1 :
                N=list(N)
                for j in range(criter_index, criter_index+len(i)) : N[j]='a'
                for _ in range(len(i)): N.remove('a')
                result=''
                for j in N: result+=j
                N=result
                result_list.append(N)
                #print(N)
                break

            elif temp_int >= temp_int_1 :
                criter_index=N.find(i, criter_index+1)
                if criter_index==-1:
                    N=list(N.replace(i,'a'))
                    cnt=0
                    for j in range(len(N)) :
                        if N[j]=='a' :
                            cnt+=1
                            if cnt==N.count('a'): N[j]='b'
                    result=''
                    for j in N :
                        if j != 'b':
                            result+=j
                    result=result.replace('a', i)
                    N=result
                    result_list.append(N)
                    #print(N)
                    break

        else:
            N=list(N.replace(i,'a'))
            cnt=0; num_a=N.count('a')
            for j in range(len(N)) :
                if N[j]=='a' :
                    cnt+=1
                    if cnt==num_a:
                        N[j]='b'
                        break
            result=''
            for j in N :
                if j != 'b':
                    result+=j
            result=result.replace('a', i)
            N=result
            result_list.append(N)
            #print(N)
            
print(int(result_list[len(result_list)-1]))
