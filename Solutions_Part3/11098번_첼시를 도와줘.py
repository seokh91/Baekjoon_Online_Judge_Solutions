list_dict=[]
n=int(input())
for i in range(n):
    list_dict.append({})
    n_1=int(input())
    for _ in range(n_1):
        money, name=input().split()
        money=int(money)
        list_dict[i].setdefault(name,money)

for i in range(n):
    print(max(list_dict[i], key=list_dict[i].__getitem__))
