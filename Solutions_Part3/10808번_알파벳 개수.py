alpha='abcdefghijklmnopqrstuvwxyz'
index_l=[]
for _ in range(26):
    index_l.append(0)
word=input()

for i in word:
    index_l[alpha.index(i)]+=1
for i in index_l:
    print(i, end=' ')
