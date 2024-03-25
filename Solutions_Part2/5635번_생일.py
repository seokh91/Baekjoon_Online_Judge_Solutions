n=int(input())
dic={}
for _ in range(n):
    name, dd, mm, yy = input().split()
    dd=int(dd); mm=int(mm); yy=int(yy)
    dic.setdefault((yy,mm,dd), name)

dic_list=sorted(list(dic))

print(dic[dic_list[len(dic_list)-1]])
print(dic[dic_list[0]])
