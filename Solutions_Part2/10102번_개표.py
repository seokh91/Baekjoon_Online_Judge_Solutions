n=int(input())
dic={'A':0, 'B':0}
voting=list(input())

for i in range(len(voting)):
    dic[voting[i]]+=1

if dic['A'] > dic['B'] : print('A')
elif dic['A'] == dic['B'] : print('Tie')
else : print('B')
