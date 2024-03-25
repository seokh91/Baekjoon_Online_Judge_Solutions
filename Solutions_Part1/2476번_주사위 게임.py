n=int(input())
l=[]
for _ in range(n):
    a,b,c=input().split()
    l.append((int(a), int(b), int(c)))

def prize_money(die_nums):
    dic={1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

    for i in range(3):
        dic[die_nums[i]] += 1

    values_list = list(dic.values())
    for i in range(6):
        if values_list[i]==3:
            index=i+1
            money=10000+index*1000
            break
        elif values_list[i]==2:
            index=i+1
            money=1000+index*100
            break
        elif values_list[i]==1:
            index=i+1
            money=index*100   
    
    return money

for i in range(n):
    l[i]=prize_money(l[i])

print(max(l))
    
