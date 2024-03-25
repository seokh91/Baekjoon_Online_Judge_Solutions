upper='QWERTYUIOPASDFGHJKLZXCVBNM'
low='qwertyuiopasdfghjklzxcvbnm'
word=list(input())

for i in range(len(word)):
    if word[i] in upper:
        word[i]=low[upper.index(word[i])]
    elif word[i] in low:
        word[i]=upper[low.index(word[i])]
result=''
for i in word:
    result+=i
print(result)
