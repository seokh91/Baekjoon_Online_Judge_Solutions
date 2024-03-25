l=['a', 'e', 'i', 'o', 'u']
word=input()
cnt=0
for i in word:
    if i in l : cnt+=1
print(cnt)
