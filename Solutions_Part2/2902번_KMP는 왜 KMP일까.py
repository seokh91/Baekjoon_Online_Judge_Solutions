result=''; alpha='QWERTYUIOPASDFGHJKLZXCVBNM'
word=list(input())
for i in word:
    if i in alpha:
        result+=i
print(result)
