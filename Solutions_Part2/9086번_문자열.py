n=int(input())
words=[]
for _ in range(n):
    words.append(input())
for i in words:
    print(i[0],end='')
    print(i[len(i)-1])
